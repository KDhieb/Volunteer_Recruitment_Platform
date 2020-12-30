from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from volunteer.models import NPO, Volunteer, Listing, User
from .decorators import npo_required, volunteer_required
from .forms import NewListingForm, VolunteerSignUpForm, NPOSignUpForm, SearchForm, EditProfileForm
from django.contrib import messages


# Create your views here.


def index(request):
    listings = Listing.objects.all().order_by("-pub_date")
    context = {'listings': listings}
    if request.method == "POST":
        form = SearchForm(request)
        if form.is_valid():
            searchParams = form.getSearchParams()

            listings = Listing.objects.filter(title__contains=searchParams['keyword'],
                                              commitment=searchParams['commitment'],
                                              city__contains=searchParams['location'])
            context = {"listings": listings, 'form': form}
            return render(request, "volunteer/search.html", context)
        else:
            messages.error(request, "Invalid form.")
    form = SearchForm()
    context['form'] = form
    return render(request, "volunteer/index.html", context)



def about(request):
    return render(request, "volunteer/about.html")


def npoProfile(request, npo_id):
    npo = NPO.objects.get(user_id=npo_id)
    listings = Listing.objects.filter(org=npo_id)
    context = {'npo': npo, 'listings': listings}
    return render(request, "volunteer/npoprofile.html", context)


def volunteerProfile(request, volunteer_id):
    volunteer = Volunteer.objects.get(user_id=volunteer_id)
    context = {'volunteer': volunteer}
    return render(request, "volunteer/volunteerprofile.html", context)



def displayListing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    context = {'listing': listing}
    return render(request, "volunteer/displaylisting.html", context)


@login_required
@volunteer_required
def apply(request, volunteer_id, listing_id):
    volunteer = Volunteer.objects.get(user_id=volunteer_id)
    volunteer.registered.add(Listing.objects.get(id=listing_id))
    volunteer.save()
    context = {'volunteer': volunteer}
    return render(request, "volunteer/volunteerprofile.html", context)

def unapply(request, volunteer_id, listing_id):
    volunteer = Volunteer.objects.get(user_id=volunteer_id)
    volunteer.registered.remove(Listing.objects.get(id=listing_id))
    volunteer.save()
    context = {'volunteer': volunteer}
    return render(request, "volunteer/volunteerprofile.html", context)

@login_required
@volunteer_required
def addToFavorites(request, volunteer_id, listing_id):
    volunteer = Volunteer.objects.get(user_id=volunteer_id)
    volunteer.favorites.add(Listing.objects.get(id=listing_id))
    volunteer.save()
    context = {'volunteer': volunteer}
    return render(request, "volunteer/volunteerprofile.html", context)

@login_required
@volunteer_required
def removeFromFavorites(request, volunteer_id, listing_id):
    volunteer = Volunteer.objects.get(user_id=volunteer_id)
    volunteer.favorites.remove(Listing.objects.get(id=listing_id))
    volunteer.save()
    context = {'volunteer': volunteer}
    return render(request, "volunteer/volunteerprofile.html", context)


@login_required
@npo_required
def newListing(request, org_id):
    if request.user.id != org_id:
        # listings = Listing.objects.all().order_by("-pub_date")
        # context = {'listings': listings}
        return render(request, "volunteer/404.html")
    if request.method != 'POST':
        form = NewListingForm()
    else:
        form = NewListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(request)
            return HttpResponseRedirect(reverse('volunteer:displaylisting', args=[listing.id]))
    context = {"form": form}
    return render(request, "volunteer/newlisting.html", context)


@login_required
@npo_required
def editListing(request, listing_id):
    """The edit listing view"""
    listing = Listing.objects.get(id=listing_id)
    if request.method != 'POST':
        form = NewListingForm(instance=listing)
    else:
        form = NewListingForm(instance=listing, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(request)
            return HttpResponseRedirect(reverse('volunteer:displaylisting', args=[listing.id]))
    context = {"listing": listing, "form": form}
    return render(request, "volunteer/editlisting.html", context)


@login_required
@npo_required
def deleteListing(request, listing_id):
    """View function to delete listing"""
    listing = Listing.objects.get(id=listing_id)
    org = listing.org
    if request.method == 'POST':
        listing.delete()
        return HttpResponseRedirect(reverse('volunteer:npoprofile', args=[org.id]))
    return render(request, "volunteer/index.html", {'listing': listing})


def signup(request):
    return render(request, "volunteer/signup.html")


class VolunteerSignupView(CreateView):
    model = User
    form_class = VolunteerSignUpForm
    template_name = 'volunteer/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'volunteer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('volunteer:index')

class NPOSignUpView(CreateView):
    model = User
    form_class = NPOSignUpForm
    template_name = 'volunteer/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'NPO'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('volunteer:index')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("volunteer:index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="volunteer/login.html", context={"login_form": form})


def search(request):
    # listings = Listing.objects.all().order_by("-pub_date")
    # context = {'listings': listings}
    #
    if request.method != 'POST':
        form = SearchForm()
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            searchParams = form.getSearchParams(request)
            listings = Listing.objects.filter(title__contains=searchParams['keyword'],
                                              commitment=searchParams['commitment'],
                                              city__contains=searchParams['location'])


            context = {"listings": listings, 'searchParams': searchParams}
            context['form'] = form
            return render(request, "volunteer/search.html", context)
    context = {'form':form}
    # context['form'] = form
    return render(request, 'volunteer/search.html', context)


@login_required
@npo_required
def editProfileNPO(request, npo_id):
    """The edit npo profile view """
    if isCorrectUser(request, npo_id):
        if request.method == "POST":
            form = EditProfileForm(request.POST, instance=request.user.npo)
            if form.is_valid():
                form.save(request)
                return HttpResponseRedirect(reverse('volunteer:npoprofile', args=[npo_id]))
        npo = NPO.objects.get(user=request.user)
        form = EditProfileForm(instance=npo.user)
        context = {"form": form}
        return render(request, "volunteer/editprofile-npo.html", context)
    else:
        return render(request, "volunteer/404.html")


@login_required
@volunteer_required()
def editProfileVolunteer(request, volunteer_id):
    """The edit volunteer profile view """
    if isCorrectUser(request, volunteer_id):
        if request.method == "POST":
            form = EditProfileForm(request.POST, instance=request.user.volunteer)
            if form.is_valid():
                form.save(request)
                return HttpResponseRedirect(reverse('volunteer:volunteerprofile', args=[volunteer_id]))
        volunteer = Volunteer.objects.get(user=request.user)
        form = EditProfileForm(instance=volunteer.user)
        context = {"form": form}
        return render(request, "volunteer/editprofile-npo.html", context)
    else:
        return render(request, "volunteer/404.html")


def isCorrectUser(request, id):
    """Helper function to check if current active user id matches given id"""
    return request.user.id == id

def error_400(request, exception):
    data = {}
    return render(request, 'volunteer/400.html', data)

def error_403(request, exception):
    data = {}
    return render(request, 'volunteer/403.html', data)

def error_404(request, exception):
    data = {}
    return render(request, 'volunteer/404.html', data)

def error_500(request):
    data = {}
    return render(request, 'volunteer/500.html', data)





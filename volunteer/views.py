from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from volunteer.models import NPO, Volunteer, Listing, User
from .decorators import npo_required
from .forms import NewListingForm, VolunteerSignUpForm, NPOSignUpForm
from django.contrib import messages


# Create your views here.


def index(request):
    listings = Listing.objects.all().order_by("-pub_date")
    context = {'listings': listings}
    return render(request, "volunteer/index.html", context)


def about(request):
    return render(request, "volunteer/about.html")


@login_required
@npo_required
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
    return render(request, "volunteer/displayListing.html", context)


@login_required
@npo_required
def newListing(request):
    if request.method != 'POST':
        form = NewListingForm()
    else:
        form = NewListingForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            org = form.cleaned_data['org']
            city = form.cleaned_data['city']
            requirements = form.cleaned_data['requirements']
            text = form.cleaned_data['text']

            new_listing = Listing()
            new_listing.title = title
            new_listing.org = org
            new_listing.city = city
            new_listing.requirements = requirements
            new_listing.text = text
            new_listing.save()
            return HttpResponseRedirect(reverse('volunteer:displaylisting', args=[new_listing.id]))
    context = {"form": form}
    return render(request, "volunteer/newlisting.html", context)


@login_required
@npo_required
def editListing(request, listing_id):
    """The article edit listing"""
    listing = Listing.objects.get(id=listing_id)
    if request.method != 'POST':
        form = NewListingForm(instance=listing)
    else:
        form = NewListingForm(instance=listing, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
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
    return render(request, "volunteer/editlisting.html", {'listing': listing})


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

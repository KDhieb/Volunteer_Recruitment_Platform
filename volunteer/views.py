from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from volunteer.models import NPO, Volunteer, Listing
from .forms import NewListingForm


# Create your views here.


def index(request):
    listings = Listing.objects.all().order_by("-pub_date")
    context = {'listings': listings}
    return render(request, "volunteer/index.html", context)


def about(request):
    return render(request, "volunteer/about.html")


def npoProfile(request, npo_id):
    npo = NPO.objects.get(id=npo_id)
    listings = Listing.objects.filter(org=npo_id)
    context = {'npo': npo, 'listings': listings}
    return render(request, "volunteer/npoprofile.html", context)


"""
def volunteerProfile(request, volunteer_id):
    volunteer = Volunteer.objects.get(id=volunteer_id)
    context = {'volunteer': volunteer}
    return render(request, "volunteer/volunteerprofile.html", context)
"""


def displayListing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    context = {'listing': listing}
    return render(request, "volunteer/displayListing.html", context)


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

def editListing(request, listing_id):
    """The article edit listing"""
    listing = Listing.objects.get(id=listing_id)
    if request.method != 'POST':
        form = NewListingForm(instance=listing)
    else:
        form = NewListingForm(instance=listing, data = request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('volunteer:displaylisting',args=[listing.id]))
    context = {"listing": listing, "form": form}
    return render(request, "volunteer/editlisting.html", context)


def deleteListing(request, listing_id):
    """View function to delete listing"""
    listing = Listing.objects.get(id=listing_id)
    org = listing.org
    if request.method == 'POST':
        listing.delete()
        return HttpResponseRedirect(reverse('volunteer:npoprofile', args = [org.id]))
    return render(request, "volunteer/editlisting.html", {'listing': listing})

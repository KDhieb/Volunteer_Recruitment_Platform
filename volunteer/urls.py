"""Defines URL patterns for articles app"""

from django.urls import path, include

from . import views

app_name = "volunteer"
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("npo/<int:npo_id>/", views.npoProfile, name="npoprofile"),
    path("volunteer/<int:volunteer_id>/", views.volunteerProfile, name="volunteerprofile"),
    path("newlisting/<int:org_id>/", views.newListing, name="newlisting"),
    path("edit-listing/<int:listing_id>", views.editListing, name="editlisting"),
    path("delete/<int:listing_id>", views.deleteListing, name = "deletelisting"),
    path("listing/<int:listing_id>/", views.displayListing, name="displaylisting"),
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/signup/", views.signup, name = "signup"),
    path("accounts/signup/volunteer/", views.VolunteerSignupView.as_view(), name = "volunteer_signup"),
    path("accounts/signup/npo/", views.NPOSignUpView.as_view(), name = "npo_signup"),
    path("accounts/login", views.login_view, name="login"),
    path("apply-to-listing/<int:volunteer_id>/<int:listing_id>/", views.apply, name="apply"),
    path("unapply-from-listing-/<int:volunteer_id>/<int:listing_id>/", views.unapply, name="unapply"),
    path("add-to-favorites/<int:volunteer_id>/<int:listing_id>/", views.addToFavorites, name="addtofavorites"),
    path("remove-from-favorites/<int:volunteer_id>/<int:listing_id>/", views.removeFromFavorites, name="removefromfavorites")
]

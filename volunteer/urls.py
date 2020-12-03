"""Defines URL patterns for articles app"""

from django.urls import path

from . import views

app_name = "volunteer"
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("npo/<int:npo_id>/", views.npoProfile, name="npoprofile"),
    #path("volunteer/<int:volunteer_id>/", views.volunteerProfile, name="volunteerprofile"),
    path("newlisting/", views.newListing, name="newlisting"),
    path("edit-listing/<int:listing_id>", views.editListing, name="editlisting"),
    path("delete/<int:listing_id>", views.deleteListing, name = "deletelisting"),
    path("listing/<int:listing_id>/", views.displayListing, name="displaylisting"),
]

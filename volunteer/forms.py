from django import forms
from volunteer.models import NPO, Listing

from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


class NewListingForm(forms.ModelForm):

    text = forms.CharField(widget=CKEditorWidget(), label="Description")

    class Meta:
        model = Listing
        fields = ['title', 'commitment', 'org', 'city', 'requirements', 'text']



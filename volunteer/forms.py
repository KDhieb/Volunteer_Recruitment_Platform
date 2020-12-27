from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from volunteer.models import NPO, Listing, User, Volunteer

from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


class NewListingForm(forms.ModelForm):

    text = forms.CharField(widget=CKEditorWidget(), label="Description")

    class Meta:
        model = Listing
        fields = ['title', 'commitment', 'org', 'city', 'requirements', 'text']


class VolunteerSignUpForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    number = forms.CharField(max_length=15)
    address = forms.CharField(max_length=200)
    about = forms.CharField(widget=CKEditorWidget(), label="About Yourself")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['name','number', 'address','about','username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_volunteer = True
        user.name = self.cleaned_data.get('name')
        user.number = self.cleaned_data.get('number')
        user.address = self.cleaned_data.get('address')
        user.about = self.cleaned_data.get('about')
        user.save()
        volunteer = Volunteer.objects.create(user=user)
        return user

class NPOSignUpForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=100, label="Organization Name")
    number = forms.CharField(max_length=15)
    address = forms.CharField(max_length=200)
    about = forms.CharField(widget=CKEditorWidget(), label="About your organization")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['name','number', 'address','about','username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_npo = True
        user.name = self.cleaned_data.get('name')
        user.number = self.cleaned_data.get('number')
        user.address = self.cleaned_data.get('address')
        user.about = self.cleaned_data.get('about')
        user.save()
        npo = NPO.objects.create(user=user)
        return user





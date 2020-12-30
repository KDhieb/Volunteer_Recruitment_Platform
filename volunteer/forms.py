from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from volunteer.models import NPO, Listing, User, Volunteer, CHOICES

from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


class NewListingForm(forms.ModelForm):

    text = forms.CharField(widget=CKEditorWidget(), label="Description")

    class Meta:
        model = Listing
        fields = ['title','commitment', 'city', 'requirements', 'text']

    @transaction.atomic
    def save(self, request):
        listing = super().save(commit=False)
        listing.title = self.cleaned_data['title']
        listing.text = self.cleaned_data['text']
        listing.requirements = self.cleaned_data['requirements']
        listing.org = request.user.npo
        listing.city = self.cleaned_data['city']
        listing.save()
        return listing

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

class EditProfileForm(forms.ModelForm):

    email = forms.EmailField()
    name = forms.CharField(max_length=100, label="Name")
    number = forms.CharField(max_length=15)
    address = forms.CharField(max_length=200)
    about = forms.CharField(widget=CKEditorWidget(), label="About")

    class Meta:
        model = User
        fields = ['name','number', 'address','about','username', 'email',]

    @transaction.atomic
    def save(self, request, commit=True):
        user = request.user
        user.name = self.cleaned_data.get('name')
        user.number = self.cleaned_data.get('number')
        user.address = self.cleaned_data.get('address')
        user.about = self.cleaned_data.get('about')
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.save()
        return user


class SearchForm(forms.ModelForm):
    keyword = forms.CharField()
    commitment = forms.ChoiceField(choices=CHOICES)
    location = forms.CharField()

    class Meta:
        model = Listing
        fields = ['keyword', 'commitment', 'location']

    @transaction.atomic
    def getSearchParams(self, request):
        searchParams = {}
        searchParams['keyword'] =  self.cleaned_data.get('keyword')
        searchParams['commitment'] = self.cleaned_data.get('commitment')
        searchParams['location'] = self.cleaned_data.get('location')
        return searchParams






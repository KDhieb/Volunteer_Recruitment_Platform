from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.
from volunteer.models import ACCESS


# class NewNPOAccountForm(UserCreationForm):
#     username = forms.CharField(required=True, label="Username")
#     email = forms.EmailField(required=True, label="Email Address")
#     name = forms.CharField(required=True, label="Organization Name")
#     number = forms.CharField(max_length=50, label= "Phone Number")
#     address = forms.CharField(max_length=500, label= "Address")
#     about = forms.CharField(widget=forms.Textarea(attrs={'placeholder': ' About your NPO...'}))
#
#     class Meta:
#         model = UserAccount
#         fields = ("name", "username","email", "number", "address", "password1", "password2", "about")
#
#
#     def save(self, commit=True):
#         user = super(NewNPOAccountForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#
#         account = UserAccount(ACCESS['NPO'])
#         account.email = self.cleaned_data['email']
#         account.username = self.cleaned_data['username']
#         npo_model = account.user_gfk
#
#         self.populateModel(npo_model)
#
#         if commit:
#             user.save()
#             account.save()
#             npo_model.save()
#             print("ID: " + str(npo_model.id))
#             print("Name: " + str(npo_model.name))
#             print("Number: " + str(npo_model.number))
#             print("Email: " + str(npo_model.email))
#             print("Username: " + str(account.username))
#         return user
#
#
#     def populateModel(self, entity_model):
#         entity_model.email = self.cleaned_data['email']
#         entity_model.name = self.cleaned_data['name']
#         entity_model.number = self.cleaned_data['number']
#         entity_model.address = self.cleaned_data['address']
#         entity_model.email = self.cleaned_data['email']
#         entity_model.about = self.cleaned_data['about']
#

# class NewVolunteerAccountForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")
#
#     def save(self, commit=True):
#         user = super(NewVolunteerAccountForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user


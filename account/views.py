from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages #import messages

# Create your views here.

# Create your views here.
#from account.forms import NewNPOAccountForm


def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('volunteer:index'))


# def register_npo(request):
#     if request.method == "POST":
#         form = NewNPOAccountForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful.")
#             return redirect("volunteer:index")
#         messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = NewNPOAccountForm
#     return render(request=request, template_name="volunteer/nporegister.html", context={"register_form": form})


# def login_npo(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}.")
#                 return redirect("volunteer:index")
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request, template_name="volunteer/npologin.html", context={"login_form": form})


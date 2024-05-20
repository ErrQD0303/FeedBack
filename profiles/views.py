from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import UserProfile

# Create your views here.


class CreateProfileView(CreateView):
    # template which will be renderred when you're not submitting the form, like using get to access the page, or when the form is not valid
    template_name = "profiles/create_profile.html"
    # model you're using to create the form
    model = UserProfile
    # the fields you want to show in the form
    fields = "__all__"
    # The url which will be redirected when the form is valid
    success_url = "/profiles"


class ProfileView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"

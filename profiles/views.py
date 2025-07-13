"""Views for the profiles app."""

from django.shortcuts import render
from .models import Profile


def index(request):
    """Display a list of all user profiles."""
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """Display details for a specific user profile."""
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)

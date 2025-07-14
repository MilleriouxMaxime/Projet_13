"""Views for the profiles app."""

import logging
from django.shortcuts import render
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """Display a list of all user profiles."""
    logger.info("Accessing profiles index view")
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """Display details for a specific user profile."""
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info(f"Accessing profile view for username={username}")
    except Profile.DoesNotExist:
        logger.error(f"Profile for username={username} does not exist")
        raise
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)

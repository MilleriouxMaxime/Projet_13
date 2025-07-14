"""Views for the lettings app."""

import logging
from django.shortcuts import render
from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """Display a list of all lettings."""
    logger.info("Accessing lettings index view")
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """Display details for a specific letting."""
    try:
        letting = Letting.objects.get(id=letting_id)
        logger.info(f"Accessing letting view for letting_id={letting_id}")
    except Letting.DoesNotExist:
        logger.error(f"Letting with id={letting_id} does not exist")
        raise
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)

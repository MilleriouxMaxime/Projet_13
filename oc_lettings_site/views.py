"""Views for the main oc_lettings_site app."""

import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """Display the home page."""
    logger.info("Accessing home page view")
    return render(request, "index.html")

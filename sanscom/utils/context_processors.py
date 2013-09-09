#-*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.conf import settings


def version(request):
    """
    Context processor, returns version number
    """
    return {'version': get_version()}


def site(request):
    """
    Context processor, returns the current site
    """
    site = Site.objects.get_current()
    return {'site': site}


def get_version():
    """
    Return version number
    """
    return "%s.%s.%s" % (settings.VERSION[0], settings.VERSION[1], settings.VERSION[2])

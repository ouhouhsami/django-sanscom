#-*- coding: utf-8 -*-
from django.forms import ModelForm

from .models import UserProfile


class UserProfileCustomForm(ModelForm):
    """
    UserProfile form
    """

    class Meta:
        model = UserProfile
        exclude = ('user', 'mugshot', 'privacy')

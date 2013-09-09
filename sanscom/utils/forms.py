#-*- coding: utf-8 -*-
from django.forms import ModelForm

from geoads.models import AdPicture, AdContact
from geoads.forms import AdContactForm, AdSearchUpdateForm

import floppyforms as forms

from .widgets import ImageThumbnailFileInput


class PrettyAdPictureForm(ModelForm):
    """
    Pretty Ad Picture Form
    """
    image = forms.ImageField(widget=ImageThumbnailFileInput, required=False)

    class Meta:
        model = AdPicture
        

class HomeContactForm(AdContactForm):
    """
    Home Contact Form
    """
    class Meta:
        model = AdContact
        widgets = {
            'message': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Votre message'}),
        }
        exclude = ['user', 'content_type', 'object_pk']


class CustomAdSearchUpdateForm(AdSearchUpdateForm):
    """
    Custom Ad Search Update Form
    """
    class Media:
        js = ('js/edit_search_form.js', )
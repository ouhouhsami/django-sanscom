#-*- coding: utf-8 -*-
import floppyforms as forms
from django.utils.translation import ugettext as _

from django_filters.widgets import RangeWidget


class BaseRangeField(forms.MultiValueField):
    """
    Base abstract class for range filters. Inheriting classes must
    define form_field attribure which is a form field class to be used for
    validation.
    """
    widget = RangeWidget
    form_class = None

    def __init__(self, *args, **kwargs):
        fields = (
            self.form_class(),
            self.form_class(),
        )
        super(BaseRangeField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return slice(*data_list)
        return None


class NumericRangeField(BaseRangeField):
    form_class = forms.DecimalField


class PriceField(forms.Field):
    def to_python(self, value):
        """
        Normalize data to price field
        """
        try:
            val = str(value).replace('.', '').replace(' ', '').replace(',', '')
            return int(val)
        except:
            raise forms.ValidationError(_(u"Entrez un prix en euros."))


class SurfaceField(forms.Field):
    def to_python(self, value):
        """
        Normalize data to surface field
        """
        if not value:
            return None
        try:
            return round(float(str(value).replace(',', '.')))
        except:
            raise forms.ValidationError(_(u"Entrez une surface en mètres carré."))

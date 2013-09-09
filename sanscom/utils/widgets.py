#-*- coding: utf-8 -*-
from django.utils.translation import ugettext
from django.forms.widgets import NullBooleanSelect, Select

import floppyforms as forms
from floppyforms.widgets import Input, NumberInput


class AppendTextInput(forms.TextInput):
    template_name = 'floppyforms/append_text_input.html'


class BootstrapSpecificRangeWidget(forms.MultiWidget):
    """
    Specific Range Widget, a range widget with min and max inputs
    """
    def __init__(self, attrs=None, appended_text=None):
        widgets = (forms.TextInput(attrs={'placeholder': 'min',
                                          'class': 'input-mini'}),
                   AppendTextInput(attrs={'placeholder': 'max',
                                          'class': 'input-mini',
                                          'appended_text': appended_text}))
        super(BootstrapSpecificRangeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]

    def format_output(self, rendered_widgets):
        render = '<div class="col-md-3">%s</div><div class="col-md-6">%s</div>' % (rendered_widgets[0], rendered_widgets[1])
        return render


class IndifferentNullBooleanSelect(NullBooleanSelect):
    """
    IndifferentNullBooleanSelect
    Used to rename the 'Unknown' default choice to 'Indifferent'
    """
    def __init__(self, attrs=None):
        choices = ((u'1', ugettext(u'Indifférent')),
                   (u'2', ugettext(u'Oui')),
                   (u'3', ugettext(u'Non')))
        Select.__init__(self, attrs, choices)


class MapWidget(Input):
    """
    Abstract Map polygon widget
    """
    def __init__(self, *args, **kwargs):
        self.ads = kwargs.get('ads', None)
        self.strokeColor = kwargs.get('strokeColor', '#FF0000')
        self.fillColor = kwargs.get('fillColor', '#00FF00')
        self.lat = kwargs.get('lat', 48.856)
        self.lng = kwargs.get('lng', 2.333)
        super(MapWidget, self).__init__()

    def get_context_data(self):
        ctx = super(MapWidget, self).get_context_data()
        ctx['ads'] = self.ads
        ctx['fillColor'] = self.fillColor
        ctx['strokeColor'] = self.strokeColor
        ctx['lat'] = self.lat
        ctx['lng'] = self.lng
        return ctx

    class Media:
        js = (
            'geoads/js/poly_utils.js',
        )


class LeafletWidget(MapWidget):
    """
    Map polygon widget (using OpenStreetMap)
    """
    template_name = 'floppyforms/gis/poly_leaflet.html'

    class Media:
        js = (
            'http://cdn.leafletjs.com/leaflet-0.4/leaflet.js',
            'geoads/js/poly_leaflet.js',
            'geoads/Leaflet.draw/leaflet.draw.js'
        )
        css = {
            'all': (
                'http://cdn.leafletjs.com/leaflet-0.4/leaflet.css',
                'geoads/Leaflet.draw/leaflet.draw.css'
            )
        }


class BooleanExtendedInput(Input):
    template_name = 'bootstrap/boolean_extended_input.html'
    widget_type = "boolean_extended_number_input"


class BooleanExtendedNumberInput(NumberInput):
    template_name = 'bootstrap/boolean_extended_number_input.html'
    widget_type = "boolean_extended_number_input"


class ImageThumbnailFileInput(forms.ClearableFileInput):
    template_name = 'floppyforms/image_thumbnail.html'


class SpecificRangeWidget(forms.MultiWidget):
    """
    Specific Range Widget, a range widget with min and max inputs
    """

    def __init__(self, attrs=None):
        widgets = (forms.TextInput(attrs={'placeholder': 'min', 'class': 'input-mini'}),
                   forms.TextInput(attrs={'placeholder': 'max', 'class': 'input-mini'}))
        super(SpecificRangeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]

    def format_output(self, rendered_widgets):
        render = '<div class="col-md-3">%s</div><div class="col-md-6">%s</div>' % (rendered_widgets[0], rendered_widgets[1])
        return render

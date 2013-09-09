#-*- coding: utf-8 -*-
from django.contrib.staticfiles import finders
from django.conf import settings

from premailer import transform

from mail_factory.mails import BaseMail

from geoads.contrib.notifications.mails import (AdModifiedMessageEmail, AdModeratedMessageEmail, 
                                                BuyerToVendorMessageEmail, VendorToBuyerMessageEmail,
                                                NewPotentialBuyerToVendorMessageEmail, NewAdToBuyerMessageEmail)


class HomeAdBaseMail(BaseMail):
    """
    Base class for ad mails
    """
    def get_context_data(self, **kwargs):
        data = super(HomeAdBaseMail, self).get_context_data(**kwargs)
        data = dict(data.items() + settings.HTML_EMAIL_COLORS.items())
        return data

    def get_attachments(self, files=None):
        attach = super(HomeAdBaseMail, self).get_attachments(files)
        for attachment in settings.HTML_EMAIL_ATTACHMENTS:
            attach.append((finders.find(attachment[0]),
                           attachment[1], attachment[2]))
        return attach


    def _render_part(self, part, lang=None):
        render = super(HomeAdBaseMail, self)._render_part(part, lang)
        if part == 'body.html':
            return transform(render).strip()
        return render


class HomeAdModifiedMessageEmail(HomeAdBaseMail, AdModifiedMessageEmail):
    pass


class HomeAdModeratedMessageEmail(HomeAdBaseMail, AdModeratedMessageEmail):
    pass


class HomeBuyerToVendorMessageEmail(HomeAdBaseMail, BuyerToVendorMessageEmail):
    pass


class HomeVendorToBuyerMessageEmail(HomeAdBaseMail, VendorToBuyerMessageEmail):
    pass


class HomeNewPotentialBuyerToVendorMessageEmail(HomeAdBaseMail, NewPotentialBuyerToVendorMessageEmail):
    pass


class HomeNewAdToBuyerMessageEmail(HomeAdBaseMail, NewAdToBuyerMessageEmail):
    pass

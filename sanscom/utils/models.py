#-*- coding: utf-8 -*-
from functools import partial

from moderation.signals import post_moderation

from geoads.signals import (geoad_new_interested_user,
                            geoad_new_relevant_ad_for_search,
                            geoad_user_message, geoad_vendor_message)
from geoads.contrib.moderation.signals import moderation_in_progress
from geoads.contrib.notifications.models import (geoad_new_interested_user_callback, geoad_new_relevant_ad_for_search_callback,
                                                 geoad_user_message_callback, geoad_vendor_message_callback,
                                                 ad_post_save_callback, ad_post_moderation_callback)

from sanscom.utils.mails import (HomeAdModifiedMessageEmail, HomeAdModeratedMessageEmail,
                                 HomeBuyerToVendorMessageEmail, HomeVendorToBuyerMessageEmail,
                                 HomeNewPotentialBuyerToVendorMessageEmail, HomeNewAdToBuyerMessageEmail)


geoad_new_interested_user.connect(receiver=partial(geoad_new_interested_user_callback, mail_class=HomeNewPotentialBuyerToVendorMessageEmail), weak=False)

geoad_new_relevant_ad_for_search.connect(receiver=partial(geoad_new_relevant_ad_for_search_callback, mail_class=HomeNewAdToBuyerMessageEmail), weak=False)

geoad_user_message.connect(receiver=partial(geoad_user_message_callback, mail_class=HomeBuyerToVendorMessageEmail), weak=False)

geoad_vendor_message.connect(receiver=partial(geoad_vendor_message_callback, mail_class=HomeVendorToBuyerMessageEmail), weak=False)

moderation_in_progress.connect(receiver=partial(ad_post_save_callback, mail_class=HomeAdModifiedMessageEmail),
                               weak=False)

post_moderation.connect(receiver=partial(ad_post_moderation_callback, mail_class=HomeAdModeratedMessageEmail), weak=False)
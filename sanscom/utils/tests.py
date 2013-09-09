#-*- coding: utf-8 -*-
from django.test import TestCase

from .templatetags.utils_tags import email_local_part
from .templatetags.ads_tags import priceformat


class EmailToNameTest(TestCase):

    def test_email_local_part(self):
        email = "saul.goodman@breakingbad.com"
        self.assertEquals(email_local_part(email), 'saul goodman')


class GeoadsTemplateTagsTestCase(TestCase):

    def test_priceformat(self):
        self.assertEqual(priceformat('3000'), '3 000')

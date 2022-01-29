from django.test import TestCase

from urlshortener.forms import ShortenedUrlForm
from urlshortener.models import ShortenedUrl

class ShortenedUrlFormTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.shortened_url_form_data = {
            'url': 'https://www.google.com'
        }

    def test_shortened_url_form_get(self):
        form = ShortenedUrlForm()
        self.assertIn('url', form.fields)

    def test_shortened_url_form_post(self):
        form = ShortenedUrlForm(self.shortened_url_form_data)
        self.assertTrue(form.is_valid())

        form.save()
        self.assertEquals(ShortenedUrl.objects.count(), 1)
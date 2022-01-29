from django import forms

from applications.urlshortener.models import ShortenedUrl

class ShortenedUrlForm(forms.ModelForm):

    class Meta:
        model = ShortenedUrl
        fields = ['url']
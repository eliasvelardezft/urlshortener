from django import forms

from shortenedurls.models import ShortenedUrl

class ShortenedUrlForm(forms.ModelForm):

    class Meta:
        model = ShortenedUrl
        fields = ['url']
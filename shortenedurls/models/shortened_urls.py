import uuid
from django.db import models


class ShortenedUrl(models.Model):

    key = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    url = models.URLField()

    def __str__(self):
        return self.url

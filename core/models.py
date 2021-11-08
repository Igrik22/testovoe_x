from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class ShortLink(models.Model):
    user = models.ForeignKey(User, related_name='shortLink', on_delete=CASCADE)
    key = models.CharField(max_length=3)
    long_link = models.CharField(max_length=200)
    short_link = models.CharField(max_length=30)

    def __str__(self):
        return self.long_link


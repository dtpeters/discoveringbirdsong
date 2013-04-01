from django.db import models
from django.contrib.auth.models import User


class UserRating(models.Model):
    recording = models.ForeignKey('Recording')
    user = models.ForeignKey('UserProfile')
    liked = models.BooleanField(blank=True)





class UserProfile(models.Model):
    user = models.OneToOneField(User)

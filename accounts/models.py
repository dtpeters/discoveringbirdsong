from django.db import models
from django.contrib.auth.models import User
from birds.models import Recording

class UserRating(models.Model):
    recording = models.ForeignKey('birds.Recording')
    user = models.ForeignKey('UserProfile')
    liked = models.BooleanField(blank=True)





class UserProfile(models.Model):
    user = models.OneToOneField(User)

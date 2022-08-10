from django.db import models
from django.contrib.auth.models import User

# Player is a user, has a bio
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250)
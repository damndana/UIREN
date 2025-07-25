# models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    major = models.CharField(max_length=100, default='Undecided')
    personality = models.CharField(max_length=50, blank=True)  # Optional field

    def __str__(self):
        return self.user.username

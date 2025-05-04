from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
     = models.PositiveIntegerField()
    bio = models.TextField()

from django.db import models
from django.contrib.auth.models import User

class TutorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    bio = models.TextField()

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)
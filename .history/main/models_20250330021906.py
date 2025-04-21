from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10)  # "tutor" or "student"

    def __str__(self):
        return f"{self.email} ({self.role})"

class TutorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    major = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
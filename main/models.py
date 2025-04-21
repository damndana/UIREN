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

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='course_images/')

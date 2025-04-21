from django.db import models

class UserProfile(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10)  # "tutor" or "student"

    def __str__(self):
        return f"{self.email} ({self.role})"

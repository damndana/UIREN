# models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50,default='Undecided')
    major = models.CharField(max_length=100, default='Undecided')
    personality = models.CharField(max_length=50, blank=True)  # Optional field

    def __str__(self):
        return self.user.username

class Event(models.Model):
    name = models.CharField(max_length=100)
    points = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Space(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attended_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"

class SpaceBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.space.name}"

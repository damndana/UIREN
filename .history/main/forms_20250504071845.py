# forms.py

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class SignInForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role', 'major', 'personality']  # You can add more fields if necessary.
        
    password = forms.CharField(widget=forms.PasswordInput)

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile  # Assuming UserProfile model exists

# User registration form to create new users
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

# User profile form to gather additional data
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Assuming you have a UserProfile model
        fields = ['role', 'major', 'personality']  # Add relevant fields from your UserProfile model

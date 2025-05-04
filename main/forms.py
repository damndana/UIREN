from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile  # Assuming UserProfile model exists

# User registration form to create new users
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match")
        return cleaned_data

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
        widgets = {
            'role': forms.Select(choices=[
                ('Student', 'Student'),
                ('Teacher', 'Teacher'),
                ('Staff', 'Staff'),
            ]),
            'major': forms.Select(choices=[
                ('Undecided', 'Undecided'),
                ('Computer Science', 'Computer Science'),
                ('Engineering', 'Engineering'),
                ('Business', 'Business'),
                ('Arts', 'Arts'),
            ]),
        }

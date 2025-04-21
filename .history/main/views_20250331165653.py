from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TutorRegistrationForm, StudentRegistrationForm
from .models import TutorProfile, StudentProfile
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def register_tutor(request):
    if request.method == 'POST':
        form = TutorRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Email is already taken')
            else:
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=form.cleaned_data['password']
                )
                TutorProfile.objects.create(
                    user=user,
                    full_name=form.cleaned_data['full_name'],
                    subject=form.cleaned_data['subject'],
                    experience=form.cleaned_data['experience'],
                    bio=form.cleaned_data['bio']
                )
                login(request, user)
                return redirect('profile')
    else:
        form = TutorRegistrationForm()
    return render(request, 'register_tutor.html', {'form': form})


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Email is already taken')
            else:
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=form.cleaned_data['password']
                )
                StudentProfile.objects.create(
                    user=user,
                    full_name=form.cleaned_data['full_name'],
                    major=form.cleaned_data['major'],
                    education_level=form.cleaned_data['education_level']
                )
                login(request, user)
                return redirect('profile')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register_student.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

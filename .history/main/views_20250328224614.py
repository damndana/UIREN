from django.shortcuts import render,redirect
from .models 

def home(request):
    return render(request, 'home.html')

def courses(request):
    return render(request, 'courses.html')

def categories(request):
    return render(request, 'categories.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

def signin(request):
    return render(request, 'signin.html')

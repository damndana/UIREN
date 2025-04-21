from django.shortcuts import render, redirect
from .models import UserProfile

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
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Debug: check if role is missing
        if not role:
            return render(request, 'signin.html', {'error': 'Please select a role.'})

        # Save to DB
        UserProfile.objects.create(email=email, password=password, role=role)

        # Redirect based on role
        if role == 'tutor':
            return redirect('register_tutor')
        else:
            return redirect('register_student')
        
    return render(request, 'signin.html')

def register_tutor(request):
    return render(request, 'register_tutor.html')

def register_student(request):
    return render(request, 'register_student.html')

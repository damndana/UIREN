from django.shortcuts import render, redirect
from django.http import HttpResponse  # ← Add this!
from .models import UserProfile
from django.contrib.auth import login
from .forms import TutorRegistrationForm, StudentRegistrationForm
from .models import TutorProfile, StudentProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")  # ✅ grab role here!

        if not (email and password and role):
            return HttpResponse("Missing fields", status=400)

        UserProfile.objects.create(email=email, password=password, role=role)
        return redirect("profile")  # or wherever you want to go

    return render(request, "signin.html")

def register_tutor(request):
    return render(request, 'register_tutor.html')

def register_student(request):
    return render(request, 'register_student.html')

def register_tutor(request):
    if request.method == 'POST':
        form = TutorRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['full_name']
            )
            tutor = form.save(commit=False)
            tutor.user = user
            tutor.save()
            login(request, user)
            return redirect('profile')  # Перенаправляем на профиль
    else:
        form = TutorRegistrationForm()
    return render(request, 'register_tutor.html', {'form': form})

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['full_name']
            )
            student = form.save(commit=False)
            student.user = user
            student.save()
            login(request, user)
            return redirect('profile')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register_student.html', {'form': form})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TutorRegistrationForm, StudentRegistrationForm
from .models import TutorProfile, StudentProfile
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# === Home Page ===
def home(request):
    return render(request, 'home.html')

# === Courses Page ===
def courses(request):
    return render(request, 'courses.html')

# === Categories Page ===
def categories(request):
    return render(request, 'categories.html')

# === About Page ===
def about(request):
    return render(request, 'about.html')

# === Sign In ===
def signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not (email and password):
            return HttpResponse("Missing fields", status=400)

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return redirect("profile")
            else:
                return HttpResponse("Incorrect password", status=401)
        except User.DoesNotExist:
            return HttpResponse("User not found", status=404)

    return render(request, "signin.html")

# === Register Tutor ===
def register_tutor(request):
    if request.method == 'POST':
        form = TutorRegistrationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            subject = form.cleaned_data['subject']
            experience = form.cleaned_data['experience']
            bio = form.cleaned_data['bio']

            if User.objects.filter(username=email).exists():
                return HttpResponse("User already exists", status=400)

            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=full_name
            )

            TutorProfile.objects.create(
                user=user,
                expertise=subject,
                experience_years=experience,
                bio=bio
            )

            login(request, user)
            return redirect('profile')
    else:
        form = TutorRegistrationForm()
    return render(request, 'register_tutor.html', {'form': form})

# === Register Student ===
def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            if User.objects.filter(username=email).exists():
                return HttpResponse("User already exists", status=400)

            user = User.objects.create_user(
                username=email,
                email=email,
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

# === Profile View ===
@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})
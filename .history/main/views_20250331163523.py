from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TutorRegistrationForm, StudentRegistrationForm
from .models import TutorProfile, StudentProfile
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def courses(request):
    return render(request, 'courses.html')

def categories(request):
    return render(request, 'categories.html')

def about(request):
    return render(request, 'about.html')

def signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not (email and password):
            return HttpResponse("Missing fields", status=400)

        # ✅ Authenticate user based on email and password (not role)
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

            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )

            TutorProfile.objects.create(
                user=user,
                full_name=full_name,
                subject=subject,
                experience=experience,
                bio=bio
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

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

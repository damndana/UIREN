from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Course, TutorProfile, StudentProfile
from django.contrib.auth.models import User
from .forms import TutorRegistrationForm, StudentRegistrationForm

# === Home Page ===
def home(request):
    return render(request, 'home.html')

# === Courses Page ===
def course_list(request):
    courses = Course.objects.all()  # Fetching all courses
    return render(request, 'courses.html', {'courses': courses})

# === Course Detail ===
def course_detail(request, slug):
    course = Course.objects.get(slug=slug)
    return render(request, 'course_detail.html', {'course': course})

# === Register for Course ===
def register_course(request, course_id):
    course = Course.objects.get(id=course_id)
    user = request.user
    # Logic for course registration (e.g. saving to a student profile or adding registration)
    return redirect('courses')

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

# === Profile Page ===
@login_required
def profile_view(request):
    if request.method == "POST":
        # Allow users to update their profile
        user_profile = request.user.studentprofile or request.user.tutorprofile
        # Save any updates from the form (update profile info)
    return render(request, "profile.html", {'user': request.user})

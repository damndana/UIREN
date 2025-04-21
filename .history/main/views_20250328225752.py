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

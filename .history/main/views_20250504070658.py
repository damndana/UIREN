from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserProfileForm
from .models import UserProfile  # Import the UserProfile model

# Registration view
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})

# Sign-in view
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error': 'Invalid credentials'})
    return render(request, 'signin.html')

# Home view
def home(request):
    return render(request, 'home.html')

# Profile view
def profile_view(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'profile.html', {'profile': user_profile})
    else:
        return redirect('signin')

# Clubs view
def clubs(request):
    # Define the logic and content of the clubs page here
    return render(request, 'clubs.html')  # Ensure 'clubs.html' exists in your templates folder

# Events view
def events(request):
    # Define the logic and content of the events page here
    return render(request, 'events.html')  # Ensure 'events.html' exists in your templates folder

# AI Helper view
def ai_helper(request):
    # Define the logic and content of the AI Helper page here
    return render(request, 'ai_helper.html')  # Ensure 'ai_helper.html' exists in your templates folder

# Map view
def map(request):
    # Define the logic and content of the map page here
    return render(request, 'map.html')  # Ensure 'map.html' exists in your templates folder

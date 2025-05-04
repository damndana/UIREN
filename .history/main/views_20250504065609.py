from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Event

# Homepage view to show upcoming events

# Sign-in view
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')  # Redirect to homepage after login
        else:
            return render(request, 'signin.html', {'error': 'Invalid credentials'})
    return render(request, 'signin.html')

# Log-in view (for the case if you need a separate view for this)
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

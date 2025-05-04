from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Event, Space, UserEvent, SpaceBooking  # Import new models
from django.contrib import messages
from .forms import UserRegistrationForm, UserProfileForm  # Import the forms for registration
from django.views.decorators.http import require_POST
import logging
from django.utils import timezone

logger = logging.getLogger(__name__)

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(
                user=user,
                role=form.cleaned_data.get('role', 'Student'),
                major=form.cleaned_data.get('major', '')
            )
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Sign-in view
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully signed in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'signin.html')

# Home view
def home(request):
    # Get upcoming events, excluding those without dates
    upcoming_events = Event.objects.exclude(date__isnull=True).filter(
        date__gte=timezone.now()
    ).order_by('date')[:3]
    
    # If we don't have enough upcoming events, add some without dates
    if upcoming_events.count() < 3:
        additional_events = Event.objects.filter(date__isnull=True)[:3-upcoming_events.count()]
        upcoming_events = list(upcoming_events) + list(additional_events)
    
    return render(request, 'home.html', {
        'upcoming_events': upcoming_events,
    })

# Profile view
@login_required
def profile_view(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
    attended_events = UserEvent.objects.filter(user=request.user)
    total_points = sum(event.event.points for event in attended_events)
    available_spaces = Space.objects.all()
    return render(request, 'profile.html', {
        'user_profile': user_profile,
        'attended_events': attended_events,
        'total_points': total_points,
        'available_spaces': available_spaces
    })

# Clubs view
@login_required
def clubs(request):
    return render(request, 'clubs.html')

# Events view
@login_required
def events(request):
    all_events = Event.objects.all()
    return render(request, 'events.html', {'events': all_events})

# AI Helper view
@login_required
def ai_helper(request):
    return render(request, 'ai_helper.html')

# Map view
@login_required
def map(request):
    return render(request, 'map.html')

@require_POST
def book_space(request, space_id):
    try:
        space = Space.objects.get(id=space_id)
        SpaceBooking.objects.create(user=request.user, space=space)
        messages.success(request, f'Successfully booked {space.name}!')
    except Space.DoesNotExist:
        messages.error(request, 'Space not found.')
    except Exception as e:
        logger.error(f"Error booking space: {str(e)}")
        messages.error(request, 'Error booking space. Please try again.')
    return redirect('profile')

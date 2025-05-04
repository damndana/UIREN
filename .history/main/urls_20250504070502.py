from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('signin/', views.signin, name='signin'),  # Keep signin for login
    path('login/', views.signin, name='login'),  # You may want this to be signin, unless login has a different view
    path('clubs/', views.clubs, name='clubs'),  # Add proper views for clubs
    path('events/', views.events, name='events'),  # Add proper views for events
    path('ai_helper/', views.ai_helper, name='ai_helper'),  # Add proper views for ai_helper
    path('map/', views.map, name='map'),  # Add proper views for map
    path('register/', views.register, name='register'),  # Registration view remains unchanged
]

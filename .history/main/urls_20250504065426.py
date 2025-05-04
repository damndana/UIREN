from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.signup, name='login'),
    path('clubs/', views.signup, name='clubs'),
    path('events/', views.signup, name='events'),
    path('ai_helper/', views.signup, name='ai_helper'),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('categories/', views.categories, name='categories'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    pa
]

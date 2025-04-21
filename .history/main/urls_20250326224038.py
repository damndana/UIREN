from django.urls import path
from . import views

urlpatterns = [
    path('/Users/dana/uiren_full/main/templates/home.html', views.home, name='home'),
    path('', views.courses, name='courses'),
    path('categories/', views.categories, name='categories'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
]

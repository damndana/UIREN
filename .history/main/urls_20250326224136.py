from django.urls import path
from . import views

urlpatterns = [
    path('/Users/dana/uiren_full/main/templates/home.html', views.home, name='home'),
    path('/Users/dana/uiren_full/main/templates/courses.html', views.courses, name='courses'),
    path('/Users/dana/uiren_full/main/templates/categories.html', views.categories, name='categories'),
    path('/Users/dana/uiren_full/main/templates/about.html', views.about, name='about'),
    path('/Users/dana/uiren_full/main/templates/profile.html', views.profile, name='profile'),
    
]

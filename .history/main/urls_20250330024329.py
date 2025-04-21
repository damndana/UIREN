from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('categories/', views.categories, name='categories'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('signin/', views.signin, name='signin'),
    path('signin/', views.signin, name='signin'),
    path('register/tutor/', views.register_tutor, name='register_tutor'),
    path('register/student/', views.register_student, name='register_student'),
    path('profile/', views.profile_view33, name='profile'),
]

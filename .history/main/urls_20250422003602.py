from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('categories/', views.categories, name='categories'),
    path('about/', views.about, name='about'),
    path('signin/', views.signin, name='signin'),
    path('signin/', views.signin, name='signin'),
    path('register/tutor/', views.register_tutor, name='register_tutor'),
    path('register/student/', views.register_student, name='register_student'),
    path('profile/', views.profile_view, name='profile'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/register/', views.register_course, name='register_course'),
]

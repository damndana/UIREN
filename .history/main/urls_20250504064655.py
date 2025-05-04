from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='courses'),
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/register/', views.register_course, name='register_course'),
    path('profile/', views.profile_view, name='profile'),
    path('signin/', views.signin, name='signin'),
]

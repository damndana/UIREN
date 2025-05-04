from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='courses'),
    path('profile/', views.profile_view, name='profile'),
    path('signin/', views.signin, name='signin'),
]

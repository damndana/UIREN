from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.signup, name='login'),
]

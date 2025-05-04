from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('clubs/', views.clubs, name='clubs'),
    path('events/', views.events, name='events'),
    path('ai_helper/', views.ai_helper, name='ai_helper'),
    path('map/', views.map, name='map'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('book-space/<int:space_id>/', views.book_space, name='book_space'),
]

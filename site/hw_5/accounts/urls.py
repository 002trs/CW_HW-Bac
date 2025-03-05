from django.urls import path
from . import views
from . import views

urlpatterns = [
    path('', views.login_view, name='auth'),  # http://127.0.0.1:8000/
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("players/", views.players),
    path('description/<int:id>/', views.description, name='description'),
]
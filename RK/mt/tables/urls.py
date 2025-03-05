from django.urls import path
from .views import table_list, available_tables

urlpatterns = [
    path('', table_list, name='table_list'),
    path('available/', available_tables, name='available_tables'),
]

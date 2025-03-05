from django.urls import path
from .views import (
    create_reservation,
    get_reservation_details,
    get_user_reservations,
    update_reservation_status,
    delete_reservation
)

urlpatterns = [
    path('', create_reservation, name='create_reservation'),
    path('<int:reservation_id>/', get_reservation_details, name='reservation_details'),
    path('user/<int:user_id>/', get_user_reservations, name='user_reservations'),
    path('<int:reservation_id>/update/', update_reservation_status, name='update_reservation'),
    path('<int:reservation_id>/delete/', delete_reservation, name='delete_reservation'),
]

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from .models import Reservation
from customers.models import Customer
from tables.models import Table


def create_reservation(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        table_id = request.POST.get('table_id')
        date_str = request.POST.get('date')

        if not (customer_id and table_id and date_str):
            return HttpResponseBadRequest("Не все поля указаны.")


        customer = get_object_or_404(Customer, id=customer_id)

        table = get_object_or_404(Table, id=table_id)


        existing_for_customer = Reservation.objects.filter(customer=customer, date=date_str).exists()
        if existing_for_customer:
            return HttpResponseBadRequest("У пользователя уже есть бронь на эту дату.")


        existing_for_table = Reservation.objects.filter(table=table, date=date_str).exists()
        if existing_for_table:
            return HttpResponseBadRequest("Столик уже забронирован на указанную дату.")

        # Создаём бронь
        new_reservation = Reservation.objects.create(
            customer=customer,
            table=table,
            date=date_str,
            status='pending'
        )
        return redirect('reservation_details', reservation_id=new_reservation.id)
    else:

        customers = Customer.objects.all()
        tables = Table.objects.all()
        return render(request, 'reservations/create_reservation.html', {
            'customers': customers,
            'tables': tables,
        })



def get_reservation_details(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'reservations/reservation_detail.html', {'reservation': reservation})


def get_user_reservations(request, user_id):
    # user_id = Customer.id
    customer = get_object_or_404(Customer, id=user_id)
    reservations = Reservation.objects.filter(customer=customer)
    return render(request, 'reservations/user_reservations.html', {
        'customer': customer,
        'reservations': reservations
    })


def update_reservation_status(request, reservation_id):
    if request.method == 'POST':
        reservation = get_object_or_404(Reservation, id=reservation_id)
        new_status = request.POST.get('status')
        if new_status not in dict(Reservation.STATUS_CHOICES):
            return HttpResponseBadRequest("Некорректный статус.")

        reservation.status = new_status
        reservation.save()
        return redirect('reservation_details', reservation_id=reservation_id)
    else:
        return HttpResponseNotAllowed(['POST'])



def delete_reservation(request, reservation_id):
    if request.method == 'POST':

        reservation = get_object_or_404(Reservation, id=reservation_id)
        reservation.delete()
        return redirect('create_reservation')
    else:
        return HttpResponseNotAllowed(['POST'])

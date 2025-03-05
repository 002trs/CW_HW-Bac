from django.shortcuts import render, redirect
from .models import Table
from datetime import datetime
from reservations.models import Reservation


def table_list(request):
    if request.method == 'POST':
        # создание нового столика
        number = request.POST.get('number')
        seats = request.POST.get('seats')
        if number and seats:
            Table.objects.create(number=number, seats=seats)
        return redirect('table_list')

    tables = Table.objects.all()
    return render(request, 'tables/table_list.html', {'tables': tables})


def available_tables(request):
    query_date = request.GET.get('date')
    if query_date:
        # Находим все столики, которые уже заняты на указанную дату
        # и отфильтровываем их из общего списка
        reservations_on_date = Reservation.objects.filter(date=query_date)
        busy_tables_ids = [r.table_id for r in reservations_on_date]
        tables = Table.objects.exclude(id__in=busy_tables_ids)
    else:
        # если не указали дату — вернём пустой/или все (зависит от требований)
        tables = []

    return render(request, 'tables/available_tables.html', {'tables': tables, 'query_date': query_date})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer


def customer_list(request):
    if request.method == 'POST':
        # создание нового пользователя
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        # можно добавить простую валидацию
        if name and phone:
            Customer.objects.create(name=name, phone=phone)
        return redirect('customer_list')

    # Если GET – отображаем список
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})


# GET /customers/{id}/
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'customers/customer_detail.html', {'customer': customer})

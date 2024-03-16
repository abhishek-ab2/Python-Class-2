import datetime

from django.shortcuts import render
from .models import Order
from .forms import OrderForm


# Create your views here.
def home(request):

    all_orders = Order.objects.all().exclude(id=10)
    return render(request, 'orders-home.html', {
        'orders': all_orders
    })


def create_order(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()

    return render(
        request,
        'orders-create.html',
        {
            'form': form
        }
    )


import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PizzaApp.settings')
django.setup()

from django.shortcuts import render, redirect
from PIZZA.forms import OrderForm
from PIZZA.models import Pizza, Topping

# main.py

def menu_view(request):
    """View function for the menu page."""
    pizzas = Pizza.objects.filter(is_available=True)
    toppings = Topping.objects.filter(is_available=True)
    return render(request, 'menu.html', {'pizzas': pizzas, 'toppings': toppings})


def confirm_order_view(request):
    """View function for the order confirmation page."""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.calculate_total()
            order.save()
            form.save_m2m()  # Save ManyToMany toppings
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'confirm.html', {'form': form})


def success_view(request):
    return render(request, 'order_success.html')
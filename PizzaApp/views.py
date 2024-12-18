from django.shortcuts import redirect
from starlette.formparsers import FormMessage

from PIZZA.models import Pizza, Topping, Order
from PIZZA.forms import OrderForm

from django.shortcuts import render
def pizza_order(request):
    form = OrderForm()  # Ensure the order form is passed to the template
    pizzas = Pizza.objects.all()  # Fetch all pizzas
    toppings = Topping.objects.all()  # Fetch all toppings

    context = {
        'form': Form,
        'pizzas': Pizza,
        'toppings': Topping,
    }
    return render(request, 'pizza/pizza_order.html', context)

def home(request):
    pizzas = Pizza.objects.all()
    toppings = Topping.objects.all()
    form = OrderForm()
    context = {
        'pizzas': Pizza,,
        'toppings': Topping,
        'form': Form,
    }
    return render(request, 'myapp/index.html', context)

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Process the order form data
            # Save the order to the database
            order = Order(
                name=form.cleaned_data['name'],
                address=form.cleaned_data['address'],
                # Add more fields as needed
            )
            order.save()
            # Redirect the user to a success page
            return redirect('order_success')
    else:
        form = OrderForm()

    context = {
        'form': form,
    }
    return render(request, 'myapp/order.html', context)
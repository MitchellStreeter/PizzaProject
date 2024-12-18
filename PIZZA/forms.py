# pizza/forms.py

from django import forms
from PIZZA.models import pizza, topping

class OrderForm(forms.Form):
    # Define the fields for the order form
    pizza = forms.ModelChoiceField(queryset=pizza.objects.all().filter(is_available=True))
    toppings = forms.ModelMultipleChoiceField(queryset=topping.objects.all().filter(is_available=True))
from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    base_price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=50)
    additional_price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.ManyToManyField(Topping, blank=True)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    order_time = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

    def calculate_total(self):
        topping_price = sum(topping.additional_price for topping in self.toppings.all())
        self.total_price = self.pizza.base_price + topping_price
        return self.total_price
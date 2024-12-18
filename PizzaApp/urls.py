from django.urls import path
from . import views

urlpatterns = [
    path('', views.pizza_order, name='pizza_order'),
]
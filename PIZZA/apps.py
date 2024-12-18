"""
This module defines the configuration for the pizza Django app.
"""

from django.apps import AppConfig

class PIZZAConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PIZZA'  # Full Python path to the app
    verbose_name = "Pizza Ordering System"

class OrderUpConfig(AppConfig):
    """
    Configuration class for the pizza Django app.
    """

    name = 'PizzaApp'
    verbose_name = "Mitchell's Pizza Project"
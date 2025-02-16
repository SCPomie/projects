from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class PizzaSize(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class PizzaCrust(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class PizzaSauce(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class PizzaCheese(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.ForeignKey("PizzaSize", on_delete=models.PROTECT)
    crust = models.ForeignKey("PizzaCrust", on_delete=models.PROTECT)
    sauce = models.ForeignKey("PizzaSauce", on_delete=models.PROTECT)
    cheese = models.ForeignKey("PizzaCheese", on_delete=models.PROTECT)

    pepperoni = models.BooleanField(default=False)
    chicken = models.BooleanField(default=False)
    ham = models.BooleanField(default=False)
    pineapple = models.BooleanField(default=False)
    peppers = models.BooleanField(default=False)
    mushrooms = models.BooleanField(default=False)
    onions = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        topping_fields = ['pepperoni', 'chicken', 'ham', 'pineapple', 'peppers', 'mushrooms', 'onions']

        topping_selected = [topping.capitalize() for topping in topping_fields if getattr(self, topping)]

        toppings_str = (",").join(topping_selected) if topping_selected else "No toppings"

        return f"{self.size} pizza with {self.crust} crust, {self.cheese} cheese, Toppings: {toppings_str}"
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()

    card_number = models.CharField(max_length=16, validators=[MinLengthValidator(16)])
    card_expiry_month = models.CharField(max_length=2, validators=[MinLengthValidator(2)])  # MM format
    card_expiry_year = models.CharField(max_length=4, validators=[MinLengthValidator(4)])  # YYYY format
    card_cvv = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} for {self.user.username} on {self.order_date.strftime('%Y-%m-%d')}"
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pizza, Order
from .forms import PizzaForm, OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form" : form})

def index(request):
    if request.user.is_authenticated:
        return redirect("home")  # Redirect logged-in users to their dashboard
    return render(request, "index.html")

@login_required
def home(request):
    orders = Order.objects.filter(user=request.user).order_by("-order_date")#filters out the user's order and sort by most recent
    return render(request, "home.html", {"orders": orders}) 

@login_required
def create_pizza(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.user = request.user
            pizza.save()
            return redirect("order", pizza_id=pizza.id)
        else:
            return render(request, "create_pizza.html", {"form":form})
    else:
        # Render the empty form for GET requests
        form = PizzaForm()
        return render(request, "create_pizza.html", {"form": form})
    
@login_required
def order(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.pizza = pizza
            order.save()
            return redirect("order_confirmation", order_id=order.id)
        else:
            return render(request, "order.html", {"form" : form, "pizza" : pizza})
    else:
        # Render an empty form for GET requests
        form = OrderForm()
    return render(request, "order.html", {"form": form, "pizza": pizza})

@login_required
def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, "order_confirmation.html", {"order" : order})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Order
from .forms import OrderForm
from django.contrib.auth.forms import UserCreationForm

def index(request):
    orders = []
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'index.html', {'orders': orders})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form":form})


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@login_required
def place_order(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.book = book
            order.save()
            return redirect('order_summary', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'form': form, 'book': book})

@login_required
def order_summary(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_summary.html', {'order': order})

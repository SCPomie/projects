from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index, name="index"),
    path("home/", views.home, name="home"),

    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('create_pizza/', views.create_pizza, name = "create_pizza"),
    path("order/<int:pizza_id>/",views.order, name="order"),
    path("order_confirmation/<int:order_id>", views.order_confirmation, name="order_confirmation")
]
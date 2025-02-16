from django import forms
from .models import Pizza, Order

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese', 
                  'pepperoni', 'chicken', 'ham', 'pineapple',
                  'peppers', 'mushrooms', 'onions']
        widgets = {
            'pepperoni': forms.CheckboxInput(),
            'chicken': forms.CheckboxInput(),
            'ham': forms.CheckboxInput(),
            'pineapple': forms.CheckboxInput(),
            'peppers': forms.CheckboxInput(),
            'mushrooms': forms.CheckboxInput(),
            'onions': forms.CheckboxInput(),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address', 'card_number', 'card_expiry_month', 'card_expiry_year', 'card_cvv']
    
    name = forms.CharField(
        max_length=100, 
        required=True, 
        help_text="Name should be max 100 characters."
    )

    address = forms.CharField(
        max_length=255, 
        required=True, 
        help_text="Address should be max 255 characters."
    )

    card_number = forms.CharField(
        max_length=16, 
        min_length=16, 
        required=True, 
        help_text="Card number should be 16 digits."
    )

    card_expiry_month = forms.IntegerField(
        min_value=1, 
        max_value=12, 
        required=True, 
        help_text="Enter a valid month (1-12)."
    )

    card_expiry_year = forms.IntegerField(
        min_value=2024, 
        max_value=2050, 
        required=True, 
        help_text="Enter a valid year between 2024 and 2050."
    )

    card_cvv = forms.CharField(
        max_length=3, 
        min_length=3, 
        required=True, 
        help_text="CVV must be 3 or 4 digits."
    )



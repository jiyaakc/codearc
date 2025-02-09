from django import forms
from .models import Product

class ProductRegistrationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'brand', 'model_number', 'serial_number', 'purchase_date', 'warranty_period']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }

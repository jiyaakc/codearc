from django import forms
from .models import ProductRegistration

class ProductRegistrationForm(forms.ModelForm):
    purchase_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = ProductRegistration
        fields = ['product_name', 'model_number', 'purchase_date', 'warranty_status']

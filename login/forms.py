from django import forms
import re
from .models import Product


class ProductRegistrationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'brand', 'model_number', 'serial_number', 'purchase_date', 'warranty_period']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }







class AgentSignupForm(forms.Form):
    pan_number = forms.CharField(max_length=10, required=True)

    def clean_pan_number(self):
        pan = self.cleaned_data.get("pan_number")
        pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
        
        if not re.match(pattern, pan):
            raise forms.ValidationError("Invalid PAN number format. Example: ABCDE1234F")
        
        return pan

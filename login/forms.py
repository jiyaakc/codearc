from django import forms
from .models import ProductRegistration
import re

class ProductRegistrationForm(forms.ModelForm):
    purchase_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = ProductRegistration
        fields = ['product_name', 'model_number', 'purchase_date', 'warranty_status']






class AgentSignupForm(forms.Form):
    pan_number = forms.CharField(max_length=10, required=True)

    def clean_pan_number(self):
        pan = self.cleaned_data.get("pan_number")
        pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
        
        if not re.match(pattern, pan):
            raise forms.ValidationError("Invalid PAN number format. Example: ABCDE1234F")
        
        return pan

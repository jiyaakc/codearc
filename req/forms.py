from django import forms
from .models import RepairRequest

class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = ['product_name', 'model_number', 'problem_description', 'photo', 'location']

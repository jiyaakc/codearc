from django.shortcuts import render
from .forms import *

def repair_request_view(request):
    form = RepairRequestForm()
    return render(request, 'repair_request.html', )

from django.urls import path
from . import views

urlpatterns = [
    path('repair-request/', views.repair_request_view, name='repair_request'),
]

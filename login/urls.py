
from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
    path('signup/', views.signup,name='signup'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
     path('register-product/', views.register_product, name='register_product'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),
    #path('home/', )
]


from django.urls import path
from .views import register_customer, register_agent, verify_otp, login_view,home,register_product,product_list

urlpatterns = [
    path('register/customer/', register_customer, name='register_customer'),
    path('register/agent/', register_agent, name='register_agent'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('login/', login_view, name='login'),
    path('home/',home,name='home'),
    path('addproduct/',register_product,name='add-product'),
    path('products/', product_list, name="product-list"),
   # path('')
]

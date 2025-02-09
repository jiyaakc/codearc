
from django.urls import path
from .views import disp, register_customer, register_agent, verify_otp, login_view,display
from .views import register_customer, register_agent, verify_otp, login_view
urlpatterns = [
    path('register/customer/', register_customer, name='register_customer'),
    path('register/agent/', register_agent, name='register_agent'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('login/', login_view, name='login'),
    path('display/',display,name="display"),
    path('disp/',disp,name="disp"),




]

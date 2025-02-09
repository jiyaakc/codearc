
from django.urls import path
<<<<<<< HEAD
from .views import register_customer, register_agent, verify_otp, login_view,display
=======
from .views import register_customer, register_agent, verify_otp, login_view
>>>>>>> b86702c3f48211d07042032c4bd9df3a26dc595b

urlpatterns = [
    path('register/customer/', register_customer, name='register_customer'),
    path('register/agent/', register_agent, name='register_agent'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('login/', login_view, name='login'),
<<<<<<< HEAD
    path('display/',display,name="display"),
=======
>>>>>>> b86702c3f48211d07042032c4bd9df3a26dc595b



]

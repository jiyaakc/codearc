from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.sessions.models import Session
import random

from . models import UserDetail


# Create your views here.


# Create your views here.
def signup(request):
    if request.method == "POST":
        UserName = request.POST.get("username")
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        ConPassword = request.POST.get("confirm-password")
        
        if Password != ConPassword:
            return render(request, "signup.html", {"error": "Passwords do not match."})
        
        # Check if the username or email already exists
        if UserDetail.objects.filter(UserName=UserName).exists():
            return render(request, "signup.html", {"error": "Username already exists."})
        elif UserDetail.objects.filter(Email=Email).exists():
            return render(request, "signup.html", {"error": "Email already exists."})
        
        # Generate OTP and save user data temporarily in the session
        otp = random.randint(100000, 999999)
        request.session['temp_user'] = {
            "UserName": UserName,
            "Email": Email,
            "Password": Password,
            "OTP": otp
        }
        
        # Send OTP to the user's email
        send_mail(
            subject="Your OTP for Signup",
            message=f"Your OTP for completing signup is {otp}.",
            from_email="shadishirin5678@gmail.com",
            recipient_list=[Email],
        )
        
        # Redirect to OTP verification page
        return redirect("verify_otp")
    
    return render(request, "signup.html")



def verify_otp(request):
    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        temp_user = request.session.get("temp_user", None)
        
        if temp_user and str(temp_user["OTP"]) == entered_otp:
            # Save the user to the database
            user = UserDetail(
                UserName=temp_user["UserName"],
                Email=temp_user["Email"],
                Password=temp_user["Password"]
            )
            user.save()
            
            # Clear the session
            del request.session["temp_user"]
            
            return render(request, "success.html", {"message": "Account created successfully!"})
        else:
            return render(request, "verify_otp.html", {"error": "Invalid OTP. Please try again."})
    
    return render(request, "verify_otp.html")


from .forms import ProductRegistrationForm

def register_product(request):
    if request.method == 'POST':
        form = ProductRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = ProductRegistrationForm()
    
    return render(request, 'user_reg.html', {'form': form})
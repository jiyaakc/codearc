import random
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from .models import CustomUser, CustomerProfile, AgentProfile
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.contrib import messages

otp_storage = {}

def send_otp(email):
    otp = random.randint(100000, 999999)
    otp_storage[email] = otp
    send_mail(
        'Your OTP Code',
        f'Your OTP is {otp}',
        'noreply@unirepair.com',
        [email],
        fail_silently=False,
    )

def register_customer(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return JsonResponse({"error": "Passwords do not match"}, status=400)

        send_otp(email)  # Send OTP
        request.session['signup_data'] = {'name': name, 'email': email, 'password': password}
        return redirect('verify_otp')
    return render(request, 'register_customer.html')

def register_agent(request):
    if request.method == "POST":
        pan_number = request.POST['pan']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        type = request.POST['type']
        company_name = request.POST.get('company_name', '')

        if password != confirm_password:
            return JsonResponse({"error": "Passwords do not match"}, status=400)

        send_otp(email)  # Send OTP
        request.session['signup_data'] = {'pan': pan_number, 'email': email, 'password': password, 'type': type, 'company_name': company_name}
        return redirect('verify_otp')
    return render(request, 'register_agent.html')

def verify_otp(request):
    if request.method == "POST":
        email = request.session['signup_data']['email']
        entered_otp = int(request.POST['otp'])

        if email in otp_storage and otp_storage[email] == entered_otp:
            data = request.session.pop('signup_data')

            user = CustomUser.objects.create(email=data['email'], password=make_password(data['password']))
            if 'name' in data:
                CustomerProfile.objects.create(user=user, name=data['name'])
            else:
                AgentProfile.objects.create(user=user, pan_number=data['pan'], type=data['type'], company_name=data['company_name'])

            return redirect('login')
        else:
            return JsonResponse({"error": "Invalid OTP"}, status=400)
    return render(request, 'verify_otp.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            # Redirect based on user type
            if hasattr(user, 'customerprofile'):
                return render(request,"customer_home.html")  # Customer home page
            elif hasattr(user, 'agentprofile'):
                return render(request,"agent_home.html")  # Agent home page
            else:
                messages.error(request, "Profile type not recognized.")
                return redirect("login")

        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "login.html")

<<<<<<< HEAD
def display(request):
         return render(request, "customer_home.html") 
=======
            
>>>>>>> b86702c3f48211d07042032c4bd9df3a26dc595b

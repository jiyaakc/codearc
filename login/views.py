import random
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from .models import CustomUser, CustomerProfile, AgentProfile
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.contrib import messages
from .forms import ProductRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Product




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

        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already exists"}, status=400)

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

        # PAN Validation Regex
        pan_pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
        if not re.match(pan_pattern, pan_number):
            messages.error(request, "Invalid PAN number format! Example: ABCDE1234F")
            return redirect('register_agent')  # Stop here and show error

        # Check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please use a different email.")
            return redirect('register_agent')  # Stop here and show error


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
                user_name = request.user.customerprofile.name

                return render(request,"customer_home.html",  {'name': user_name})  # Customer home page

                return render(request,"customer_home.html", {'name': user_name})  # Customer home page

            elif hasattr(user, 'agentprofile'):
                return render(request,"agent_home.html")  # Agent home page
            else:
                messages.error(request, "Profile type not recognized.")
                return redirect("login")

        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "login.html")


def display(request):

    user_name = request.user.customerprofile.name
    
    return render(request, "customer_home.html", {'name': user_name}) 
            

    return render(request, "customer_home.html") 


def disp(request):
        return render(request,"agent_home.html")
         


def home(request):
    return render(request, "home.html")            





from .models import Agent
import re

def agent_signup(request):
    if request.method == "POST":
        pan_number = request.POST.get("pan").upper()  # Convert to uppercase
        email = request.POST.get("email")
        password = request.POST.get("password")

        pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
        if not re.match(pattern, pan_number):
            messages.error(request, "Invalid PAN number format. Example: ABCDE1234F")
            return redirect("agent_signup")

        # Save if PAN is valid
        Agent.objects.create(pan_number=pan_number, email=email, password=password)
        messages.success(request, "Signup successful!")
        return redirect("login")

    return render(request, "signup.html")


def register_product(request):
    if request.method == "POST":
        form = ProductRegistrationForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user.customerprofile  # Link product to logged-in user
            product.save()

            return redirect('product-list')  # Redirect to product list page
    form = ProductRegistrationForm()
    return render(request, 'product_reg.html',{'form': form})

    return redirect('product-list')
    form = ProductRegistrationForm()
    return render(request, 'product_reg.html', {'form': form})



def product_list(request):
    products = Product.objects.filter(user=request.user.customerprofile)
    return render(request, 'product_list.html', {'products': products})


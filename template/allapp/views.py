from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth import logout as auth_logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import CustomUser
from .helpers import send_forget_password_mail
#from .models import Registration

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def phome(request):
    return render(request,'phome.html')
@login_required
def appointment(request):
    return render(request,'appointment.html')
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("phome")
        else:
            messages.error(request, "Invalid login credentials")

    return render(request,'login.html')
def signup(request):
    if request.method == "POST":
        username=request.POST.get('username')
        #fullname = request.POST.get('firstname')
        firstname=request.POST.get('firstname') 
        lastname = request.POST.get('lastname')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
       # phone_number = request.POST.get('phoneNumber')
        #address = request.POST.get('address')
      
        

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        elif password != confirmPassword:
            messages.error(request, "Passwords do not match")
        else:
            user = CustomUser(username=username,first_name=firstname,last_name=lastname,dob=dob,email=email,role='PATIENT')  # Change role as needed
            user.set_password(password)
            user.save()
            messages.success(request, "Registered successfully")
            return redirect("login")
    return render(request,'signup.html')

def logout_confirmation(request):
    return render(request, 'logout_confirmation.html')
def logout(request):
    auth_logout(request)  # Use the logout function to log the user out
    return redirect('logout_confirmation')  # Redirect to the confirmation page

def ChangePassword(request, token):
    context = {}

    try:
        profile_obj = CustomUser.objects.filter(forget_password_token=token).first()

        if profile_obj is None:
            messages.success(request, 'Invalid token.')
            return redirect('/forget-password/')

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')

            if new_password != confirm_password:
                messages.success(request, 'Passwords do not match.')
                return redirect(f'/change-password/{token}/')

            # Update the password for the user associated with profile_obj
            profile_obj.set_password(new_password)
            profile_obj.forget_password_token = None  # Remove the token
            profile_obj.save()
            return redirect('/login/')

    except Exception as e:
        print(e)
    
    return render(request, 'change-password.html', context)


import uuid
def ForgetPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            user_obj = CustomUser.objects.filter(username=username).first()
            
            if user_obj is None:
                messages.error(request, 'No user found with this username.')
                return redirect('/forget-password/')
            
            token = str(uuid.uuid4())
            user_obj.forget_password_token = token
            user_obj.save()
            send_forget_password_mail(user_obj.email, token)
            messages.success(request, 'An email has been sent with instructions to reset your password.')
            return redirect('/forget-password/')
    
    except Exception as e:
        print(e)
    
    return render(request, 'forget-password.html')
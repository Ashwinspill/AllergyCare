from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth import logout as auth_logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import CustomUser
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
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login, get_user_model
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import CustomUser
from .helpers import send_forget_password_mail
from .forms import PatientProfileForm
from django.views.decorators.cache import never_cache
from django.contrib.auth.hashers import check_password
from social_django.models import UserSocialAuth
from social_django.utils import psa
from django.views import View
from django.contrib.auth.backends import ModelBackend


# Create your views here.

def index(request):
    return render(request,'index.html')

# @login_required
# def phome(request):
#    if 'email' in request.session:
#        response = render(request, 'phome.html')
#        response['Cache-Control'] = 'no-store, must-revalidate'
#        return response
#    else:
#        return redirect('logout_confirmation') 
 
# def phome(request):
#     if request.user.is_authenticated:
#         response = render(request, 'phome.html')
#         response['Cache-Control'] = 'no-store, must-revalidate'
#         return response
#     else:
#         return redirect('logout_confirmation')
#     # return render(request,'phome.html')
@login_required
def phome(request):
    response = render(request, 'phome.html')
    response['Cache-Control'] = 'no-store, must-revalidate'
    return response    
@login_required
def dhome(request):
    response = render(request, 'dhome.html')
    response['Cache-Control'] = 'no-store, must-revalidate'
    return response    

# @login_required
def appointment(request):
    return render(request,'appointment.html')
def test(request):
    return render(request,'test.html')


# #login with google and normal pakka code
# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         try:
#             # Attempt to retrieve the user by email                                           #pakka sanm 
#             user = CustomUser.objects.get(email=email)

#             # Check the password
#             if user and check_password(password, user.password):
#                 auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Specify the backend
#                 return redirect('phome')
#             else:
#                 error_message = "Invalid credentials"
#                 messages.error(request, error_message)
#         except CustomUser.DoesNotExist:
#             # User with the given email does not exist
#             error_message = "User with this email does not exist"
#             messages.error(request, error_message)

#     response = render(request, 'login.html')
#     response['Cache-Control'] = 'no-store, must-revalidate'
#     return response

    
#testing new login
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Attempt to retrieve the user by email
            user = CustomUser.objects.get(email=email)

            # Check the password
            if user and check_password(password, user.password):
                auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Specify the backend

                # Redirect based on user's role and flags
                if user.is_superuser:
                    return redirect('admind')  # Redirect to admin dashboard
                elif user.is_patient:
                    return redirect('phome')  # Redirect to patient's page
                elif user.is_doctor:
                    return redirect('dhome')  # Redirect to doctor's page
                else:
                    error_message = "Invalid role"
                    messages.error(request, error_message)

            else:
                error_message = "Invalid credentials"
                messages.error(request, error_message)
        except CustomUser.DoesNotExist:
            # User with the given email does not exist
            error_message = "User with this email does not exist"
            messages.error(request, error_message)

    response = render(request, 'login.html')
    response['Cache-Control'] = 'no-store, must-revalidate'
    return response
    
    
    
#patient signup
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
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif password != confirmPassword:
            messages.error(request, "Passwords do not match")
        else:
            user = CustomUser(username=username,first_name=firstname,last_name=lastname,dob=dob,email=email,is_patient=True,role="PATIENT")  # Change role as needed
            user.set_password(password)
            user.save()
            messages.success(request, "Registered successfully")
            return redirect("login")
    return render(request,'signup.html')


#doctor signup
def signup1(request):
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
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif password != confirmPassword:
            messages.error(request, "Passwords do not match")
        else:
            user = CustomUser(username=username,first_name=firstname,last_name=lastname,dob=dob,email=email,is_doctor=True,role="DOCTOR")  # Change role as needed
            user.set_password(password)
            user.save()
            messages.success(request, "Registered successfully")
            return redirect("login")
    return render(request,'signup1.html')

@never_cache
def logout_confirmation(request):
    return render(request, 'logout_confirmation.html')
def logout(request):
    auth_logout(request) # Use the logout function to log the user out
    return redirect('logout_confirmation')  # Redirect to the confirmation page

def ChangePassword(request, token):
    context = {}

    try:
        profile_obj = CustomUser.objects.filter(forget_password_token=token).first()

        if profile_obj is None:
            messages.error(request, 'Invalid token.')
            return redirect('/forget-password/')

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')

            if new_password != confirm_password:
                messages.error(request, 'Passwords do not match.')
                return redirect(f'/change-password/{token}/')

            # Update the password for the user associated with profile_obj
            profile_obj.set_password(new_password)
            profile_obj.forget_password_token = None  # Remove the token
            profile_obj.save()

            # Set a success message
            messages.success(request, 'Password changed successfully.')

            # Redirect to login page with the success message
            return redirect('/login/', {'success_message': 'Password changed successfully'})

    except Exception as e:
        print(e)
        messages.error(request, 'An error occurred while processing your request.')
    
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
# @login_required
@never_cache
def patient_profile(request):
    patient = request.user
    
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
    else:
        form = PatientProfileForm(instance=patient)

    return render(request, 'patient_profile.html', {'patient': patient, 'form': form})

@login_required
def admind(request):
    # Query all User objects (using the custom user model) from the database
    User = get_user_model()
    user_profiles = User.objects.all()
    
    # Pass the data to the template
    context = {'user_profiles': user_profiles}
    
    # Render the HTML template
    return render(request, 'admind.html', context)

def toggle_active(request, user_id, is_active):
    try:
        user = CustomUser.objects.get(id=user_id)
        # Convert the "is_active" parameter to a boolean
        is_active = is_active.lower() == 'true'
        # Toggle the active status
        user.is_active = not is_active
        user.save()
        messages.success(request, f'User is now {"Active" if user.is_active else "Inactive"}.')
    except CustomUser.DoesNotExist:
        messages.error(request, 'User not found.')
    return redirect('admind')  # Replace 'admind' with your actual admin dashboard URL name



def google_authenticate(request):
    # Handle the Google OAuth2 authentication process
    # ...

    # After successful authentication, create or get the user
    try:
        user_social = UserSocialAuth.objects.get(provider='google-oauth2', user=request.user)
        user = user_social.user
    except UserSocialAuth.DoesNotExist:
        user = request.user

    # Set a default role for users signing in with Google (e.g., "Patient")
    user.role = 'Patient'
    user.save()

    # Redirect to the desired page (phome.html for Patient role)
    if user.role == 'Patient':
        return redirect('phome')  # Make sure you have a URL named 'phome'
    
    
    
    
    
    
    
    
    
    
# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             auth_login(request, user)
#             request.session['username'] = username
#             messages.success(request, "Login successful!")
#             return redirect("phome")  # Replace 'phome' with the name of your home page URL
#         else:
#             messages.error(request, "Invalid login credentials")

#     response = render(request, 'login.html')
#     response['Cache-Control'] = 'no-store, must-revalidate'
#     return response
            

    # return render(request,'login.html')



# try email login
# from django.contrib import messages

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         try:
#             # Attempt to retrieve the user by email
#             user = CustomUser.objects.get(email=email)

#             # Check the password
#             if user and check_password(password, user.password):
#                 request.session['email'] = email
#                 auth_login(request, user)
#                 return redirect('phome')
#             else:
#                 error_message = "Invalid credentials"
#                 messages.error(request, error_message)      
#         except CustomUser.DoesNotExist:
#             # User with the given email does not exist
#             error_message = "User with this email does not exist"
#             messages.error(request, error_message)
    
#     response = render(request, 'login.html')
#     response['Cache-Control'] = 'no-store, must-revalidate'
#     return response


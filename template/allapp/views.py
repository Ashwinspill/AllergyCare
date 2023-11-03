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
from django.contrib.auth import login
from social_django.utils import psa
from django.views import View
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from .forms import MedicineForm
from .models import Medicine




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
# def signup1(request):
#     if request.method == "POST":
#         username=request.POST.get('username')
#         #fullname = request.POST.get('firstname')
#         firstname=request.POST.get('firstname') 
#         lastname = request.POST.get('lastname')
#         dob = request.POST.get('dob')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirmPassword = request.POST.get('confirmPassword')
#        # phone_number = request.POST.get('phoneNumber')
#         #address = request.POST.get('address')
      
        

#         if CustomUser.objects.filter(email=email).exists():
#             messages.error(request, "Email already exists")
#         elif CustomUser.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists")
#         elif password != confirmPassword:
#             messages.error(request, "Passwords do not match")
#         else:
#             user = CustomUser(username=username,first_name=firstname,last_name=lastname,dob=dob,email=email,is_doctor=True,role="DOCTOR")  # Change role as needed
#             user.set_password(password)
#             user.save()
#             messages.success(request, "Registered successfully")
#             return redirect("login")
#     return render(request,'signup1.html')



# new doctor signup 
from .models import CustomUser, Doctor
def signup1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        # Check if the email or username already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif password != confirmPassword:
            messages.error(request, "Passwords do not match")
        else:
            # Create a CustomUser with role 'DOCTOR'
            user = CustomUser.objects.create_user(
                username=username,
                first_name=firstname,
                last_name=lastname,
                dob=dob,
                email=email,
                password=password,
                is_doctor=True,
                role=CustomUser.DOCTOR  # Assuming you have defined DOCTOR as 'Doctor' in your model
            )

            # Create a corresponding Doctor record
            Doctor.objects.create(
                user=user,
                first_name=firstname,
                last_name=lastname,
                dob=dob,
                email=email,
                username=username
            )

            messages.success(request, "Registered successfully")
            return redirect("login")
    
    return render(request, 'signup1.html')

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


# trial of profile 
# class PatientProfileForm(forms.ModelForm):
#     dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'email', 'username', 'dob']

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         # Add your email validation logic here, e.g., check for a specific domain or pattern
#         if not email.endswith('@example.com'):
#             raise forms.ValidationError("Email must be from example.com domain.")
#         return email

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         # Add your username validation logic here, e.g., checking for uniqueness
#         if CustomUser.objects.filter(username=username).exclude(id=self.instance.id).exists():
#             raise forms.ValidationError("Username is already in use.")
#         return username

#     def clean_dob(self):
#         dob = self.cleaned_data.get('dob')
#         # Add your date of birth validation logic here, e.g., checking if the user is of a certain age
#         # Example: Check if the user is at least 18 years old
#         from datetime import date
#         age = date.today().year - dob.year
#         if age < 18:
#             raise forms.ValidationError("You must be at least 18 years old.")
#         return dob

@never_cache
def patient_profile2(request):
    patient = request.user
    
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
    else:
        form = PatientProfileForm(instance=patient)

    return render(request, 'patient_profile2.html', {'patient': patient, 'form': form})

@login_required
def admind(request):
    # Query all User objects (using the custom user model) from the database
    User = get_user_model()
    user_profiles = User.objects.all()
    
    # Pass the data to the template
    context = {'user_profiles': user_profiles}
    
    # Render the HTML template
    # return render(request, 'admind.html', context)

    response = render(request, 'admind.html', {'user_profiles': user_profiles})
    # response = render(request, 'dhome.html')
    response['Cache-Control'] = 'no-store, must-revalidate'
    return response   

def toggle_active(request, user_id, is_active):
    user = get_object_or_404(CustomUser, id=user_id)
    is_active = is_active.lower() == 'true'

    if is_active:  # If activating the user
        # Send an activation email
        subject = 'Your Account Deactivation'
        message = 'Your account has been Deactivated. Please contact support for more information.'
    else:  # If deactivating the user
        # Send a deactivation email
        subject = 'Your Account Activation'
        message = 'Your account has been Activated by the administrator. You can now log in and use your account.'

    from_email = 'allergycare163@gmail.com'  # Use the email address you configured in settings.py
    recipient_list = [user.email]

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        user.is_active = not is_active
        user.save()

        response_data = {
            'message': f'User is now {"Active" if user.is_active else "Inactive"}.',
            'email_sent': True
        }
    except CustomUser.DoesNotExist:
        response_data = {
            'message': 'User not found',
            'email_sent': False
        }

    return JsonResponse(response_data)


def google_authenticate(request):
    # Handle the Google OAuth2 authentication process
    # ...

    # After successful authentication, create or get the user
    try:
        user_social = UserSocialAuth.objects.get(provider='google-oauth2', user=request.user)
        user = user_social.user
    except UserSocialAuth.DoesNotExist:
        user = request.user

    # Set the user's role to "Patient"
        user.role = 'Patient'
        user.save()

    # Set the user's is_patient field to True
        user.is_patient = True
        user.save()

    # Redirect to the desired page (phome.html for Patient role)
    return redirect('phome')  # Make sure you have a URL named 'phome

# def add_medicine(request):
#     if request.method == 'POST':
#         form = MedicineRegistrationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('medicine_list')  # Redirect to the medicine list page
#     else:
#         form = MedicineRegistrationForm()

#     context = {
#         'form': form,
#     }
#     return render(request, 'add_medicine.html', context)


def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')  # Redirect to the medicine list page
    else:
        form = MedicineForm()
    return render(request, 'add_medicine.html', {'form': form})

@login_required
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine_list.html', {'medicines': medicines})

@login_required
def patient_medlist(request):
    medicines = Medicine.objects.all()
    return render(request, 'patient_medlist.html', {'medicines': medicines})



# from .forms import DoctorDetailsForm
# def add_doctor_details(request):
#     if request.method == 'POST':
#         user = request.user
#         # Check if a DoctorDetails instance already exists for this user
#         if not hasattr(user, 'doctor_details'):
#             form = DoctorDetailsForm(request.POST, request.FILES)
#             if form.is_valid():
#                 doctor_details = form.save(commit=False)
#                 doctor_details.user = user
#                 doctor_details.save()
#                 return redirect('doctor_information')
#         else:
#             form = DoctorDetailsForm()
#     return render(request, 'doctor_information.html', {'form': form})



# doctor by admin starts here 
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
@login_required
def doctor_registration(request):
    if request.method == 'POST':
        provider_name = request.POST.get('providername')
        provider_email = request.POST.get('email')
        
        # Validate the input fields here if necessary
        
        # Replace 'YOUR_BASE_URL' with the actual base URL of your website
        base_url = 'http://127.0.0.1:8000/signup1'
        
        # Create a registration link
        registration_path = "register"  # Relative path for registration
        registration_link = f"{base_url}"
        
        # Render HTML content for the email
        html_message = render_to_string('doctor_registration_email.html', {
            'provider_name': provider_name,
            'registration_link': registration_link
        })
        
        # Send HTML email to the provider's email
        subject = 'Doctor Registration Link'
        plain_message = f"Click the following link to complete your registration: {registration_link}"
        from_email = settings.DEFAULT_FROM_EMAIL
        
        email = EmailMessage(subject, plain_message, from_email, [provider_email])
        email.content_subtype = "html"
        email.send(fail_silently=False)
        
        # Redirect to a success page or display a success message
        return render(request, 'doctor_registration_success.html')
    
    return render(request, 'doctor_registration_form.html')


from .forms import DoctorAdditionalDetailsForm
from .models import Doctor
@login_required
def fill_additional_details(request):
    if request.method == "POST":
        form = DoctorAdditionalDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            doctor_instance = Doctor.objects.get(user=request.user)  # Get the currently logged-in doctor

            # Create and save the DoctorAdditionalDetails instance using the form
            doctor_additional_details = form.save(commit=False)  # Create an instance without saving it
            doctor_additional_details.doctor = doctor_instance  # Link it to the doctor
            doctor_additional_details.save()

            return redirect('doctor_information')  # Redirect to the doctor information page

    else:
        form = DoctorAdditionalDetailsForm()

    return render(request, 'fill_additional_details.html', {'form': form})


from django.http import HttpResponse
from .models import Doctor, DoctorAdditionalDetails
@login_required
def doctor_information(request):
    if request.user.is_authenticated and request.user.is_doctor:
        # Get the doctor and associated additional details if they exist
        try:
            doctor = Doctor.objects.get(user=request.user)
            additional_details = DoctorAdditionalDetails.objects.get(doctor=doctor)
        except Doctor.DoesNotExist:
            doctor = None
            additional_details = None

        return render(request, 'doctor_info.html', {'doctor': doctor, 'additional_details': additional_details})
    else:
        return HttpResponse("User is not authenticated or not a doctor.")
    
    

from .forms import DoctorForm, DoctorAdditionalDetailsForm
def edit_doctor_details(request):
    user = request.user
    try:
        doctor = Doctor.objects.get(user=user)
        doctor_additional_details = DoctorAdditionalDetails.objects.get(doctor=doctor)
    except Doctor.DoesNotExist:
        # Handle the case where the doctor doesn't exist
        # You can create a doctor profile if needed
        return redirect('create_doctor_profile')
    
    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST, instance=doctor)
        details_form = DoctorAdditionalDetailsForm(request.POST, request.FILES, instance=doctor_additional_details)
        if doctor_form.is_valid() and details_form.is_valid():
            doctor_form.save()
            details_form.save()
            return redirect('doctor_information')
    else:
        doctor_form = DoctorForm(instance=doctor)
        details_form = DoctorAdditionalDetailsForm(instance=doctor_additional_details)
    
    return render(request, 'edit_doctor_details.html', {'doctor_form': doctor_form, 'details_form': details_form})

from django.views.generic import ListView
from .models import Doctor, DoctorAdditionalDetails
class AllDoctorsListView(ListView):
    template_name = 'all_doctor_list.html'
    context_object_name = 'doctors'

    def get_queryset(self):
        # Fetch all doctors and their additional details
        doctors = Doctor.objects.all()
        details = DoctorAdditionalDetails.objects.all()
        
        # Combine the data into a list of tuples (doctor, additional_details)
        doctor_data = []
        for doctor in doctors:
            additional_details = details.filter(doctor=doctor).first()
            doctor_data.append((doctor, additional_details))

        return doctor_data
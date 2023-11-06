from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.contrib.auth import get_user_model
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None,dob=None, **extra_fields):     #, role='Patient'
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email,dob=dob, **extra_fields)       # , role=role
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, role='Admin',dob=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, role=role,dob=dob, **extra_fields)

class CustomUser(AbstractUser):
    ADMIN = 'Admin'
    PATIENT = 'Patient'
    DOCTOR = 'Doctor'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (PATIENT, 'Patient'),
        (DOCTOR, 'Doctor'),
    ]

    # Fields for custom user roles
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default=PATIENT)  # Default role for regular users
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default=DOCTOR)
    forget_password_token = models.UUIDField(null=True, blank=True) #forgetpass
    email = models.EmailField(unique=True)
    # objects = CustomUserManager()
    username = models.CharField(max_length=150, unique=True)
    dob = models.DateField(null=True, blank=True)
    # Define boolean fields for specific roles
    # is_patient = models.BooleanField(default=True)
    # is_doctor = models.BooleanField(default=True)
    is_patient=models.BooleanField('is_patient',default=False,null=True)
    is_doctor=models.BooleanField('is_doctor',default=False,null=True)
    REQUIRED_FIELDS=[]
    def __str__(self):
        return self.email
    

# patient
class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add fields for id, first name, last name, email, role, dob, and username
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=15, default=CustomUser.PATIENT)
    dob = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=150, unique=True)
    
    
# doctor
class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add fields for id, first name, last name, email, role, dob, and username
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=15, default=CustomUser.DOCTOR)
    dob = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=150, unique=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
    
class Medicine(models.Model):
    med_image = models.ImageField(upload_to='shop_images/')
    name = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.CharField(max_length=255)
    company_name = models.CharField(max_length=100)
    medicine_info = models.CharField(max_length=200, default='medicine info')
    quantity = models.PositiveIntegerField(default=0)  # Add this field for quantity

    def __str__(self):
        return self.name
    
    
class DoctorAdditionalDetails(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='doctor_pictures/', null=True, blank=True)
    registration_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    experience = models.PositiveIntegerField(null=True, blank=True)
    specialty = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    
    
    
User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicines = models.ManyToManyField(Medicine, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.medicine.name} in Cart for {self.cart.user}"
    

# consult
class ConsultationRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='consultation_requests/')
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation request from {self.patient.first_name} to {self.doctor.first_name}"
    
    
class Reply(models.Model):
    consultation_request = models.ForeignKey(ConsultationRequest, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    message = models.TextField()
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    appointment_needed = models.BooleanField(default=False)

    def __str__(self):
        return f"Reply from {self.doctor.first_name} to {self.consultation_request.patient.first_name}"
    

# appointment
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot_choices = [
        ('9:00 AM - 10:00 AM', '9:00 AM - 10:00 AM'),
        ('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM'),
        ('11:00 AM - 12:00 PM', '11:00 AM - 12:00 PM'),
        ('12:00 PM - 1:00 PM', '12:00 PM - 1:00 PM'),
        ('2:00 PM - 3:00 PM', '2:00 PM - 3:00 PM'),
        ('3:00 PM - 4:00 PM', '3:00 PM - 4:00 PM'),
        ('4:00 PM - 5:00 PM', '4:00 PM - 5:00 PM'),
        ('5:00 PM - 6:00 PM', '5:00 PM - 6:00 PM'),
        ('6:00 PM - 7:00 PM', '6:00 PM - 7:00 PM'),
    ]
    time_slot = models.CharField(max_length=30, choices=time_slot_choices)
    patient_name = models.CharField(max_length=60)
    patient_email = models.EmailField()

    def __str__(self):
        return f"Appointment with {self.doctor} on {self.date} at {self.time_slot}"
    

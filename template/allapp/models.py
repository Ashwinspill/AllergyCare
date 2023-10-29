from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

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
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default=DOCTOR)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default=PATIENT)  # Default role for regular users
    forget_password_token = models.UUIDField(null=True, blank=True) #forgetpass
    email = models.EmailField(unique=True)
    # objects = CustomUserManager()
    username = models.CharField(max_length=150, unique=True)
    dob = models.DateField(null=True, blank=True)
    # Define boolean fields for specific roles
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=True)
    # is_patient=models.BooleanField('is_patient',default=False,null=True)
    # is_doctor=models.BooleanField('is_doctor',default=False,null=True)
    REQUIRED_FIELDS=[]
    def __str__(self):
        return self.email
    
    
    
class Medicine(models.Model):
    med_image = models.ImageField(upload_to='shop_images/')
    name = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.CharField(max_length=255)
    company_name = models.CharField(max_length=100)
    medicine_info = models.CharField(max_length=200, default='medicine info')
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.med_name
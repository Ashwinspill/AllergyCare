from django.contrib import admin
from .models import CustomUser
from .models import Medicine
from .models import Appointment
from .models import ConsultationRequest

admin.site.register(CustomUser)
admin.site.register(Medicine)
admin.site.register(Appointment)
admin.site.register(ConsultationRequest)

# Register your models here.

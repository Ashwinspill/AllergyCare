from django.contrib import admin
from .models import CustomUser
from .models import Medicine
from .models import Appointment
from .models import ConsultationRequest
from .models import Order

admin.site.register(CustomUser)
admin.site.register(Medicine)
admin.site.register(Appointment)
admin.site.register(ConsultationRequest)
admin.site.register(Order)
# Register your models here.

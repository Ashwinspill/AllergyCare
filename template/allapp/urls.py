from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import AllDoctorsListView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('index/', views.index,name="index"),
    path('appointment/',views.appointment,name="appointment"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('signup1/',views.signup1,name="signup1"),  #doctor signup
    path('phome/', views.phome, name='phome'),
    path('dhome/', views.dhome, name='dhome'),
    path('test/', views.test, name='test'),
    path('logout/', views.logout, name='logout'), 
    path('logout_confirmation/', views.logout_confirmation, name='logout_confirmation'),
    path('forget-password/' , views.ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , views.ChangePassword , name="change_password"),
    path('patient_profile/', views.patient_profile, name='patient_profile'), 
    path('patient_profile2/', views.patient_profile2, name='patient_profile2'), 
    path('admind/',views.admind,name="admind"),
    path('toggle-active/<int:user_id>/<str:is_active>/', views.toggle_active, name='toggle_active'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
    path('medicine_list/', views.medicine_list, name='medicine_list'),
    path('patient_medlist/', views.patient_medlist, name='patient_medlist'),
    path('admind/doctor_registration/', views.doctor_registration, name='doctor_registration'),
    path('fill_additional_details/', views.fill_additional_details, name='fill_additional_details'),
    path('doctor_information/', views.doctor_information, name='doctor_information'),
    path('edit_doctor_details/', views.edit_doctor_details, name='edit_doctor_details'),
    path('all_doctors/', AllDoctorsListView.as_view(), name='all_doctors'),
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('index/', views.index,name="index"),
    path('appointment/',views.appointment,name="appointment"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('signup1/',views.signup1,name="signup1"),
    path('phome/', views.phome, name='phome'),
    path('dhome/', views.dhome, name='dhome'),
    path('test/', views.test, name='test'),
    path('logout/', views.logout, name='logout'), 
    path('logout_confirmation/', views.logout_confirmation, name='logout_confirmation'),
    path('forget-password/' , views.ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , views.ChangePassword , name="change_password"),
    path('patient_profile/', views.patient_profile, name='patient_profile'), 
    path('admind/',views.admind,name="admind"),
    path('toggle-active/<int:user_id>/<str:is_active>/', views.toggle_active, name='toggle_active'),
    path('social-auth/', include('social_django.urls', namespace='social')),
] 
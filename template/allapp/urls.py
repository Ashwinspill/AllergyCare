from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('appointment/',views.appointment,name="appointment"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('phome/', views.phome, name='phome'),
    path('logout/', views.logout, name='logout'), 
    path('logout_confirmation/', views.logout_confirmation, name='logout_confirmation'),
    path('forget-password/' , views.ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , views.ChangePassword , name="change_password"),
] 
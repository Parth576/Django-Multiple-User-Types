from django.urls import path
from gradesApp import views

app_name='gradesApp'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('registerStudent/',views.registerStudent,name='registerStudent'),
    path('registerTeacher/',views.registerTeacher,name='registerTeacher'),
    path('login/',views.userLogin,name='userLogin'),
    path('dashboard',views.dashboard,name='dashboard'),
   
]

from django.shortcuts import render,redirect
from gradesApp.forms import studentForm,studentAddForm,teacherForm,teacherAddForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from gradesApp.models import Student,Teacher 
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,'gradesApp/index.html')

@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    return render(request,'gradesApp/register.html')

def registerStudent(request):
    registered=False
    if request.method=='POST':
        var_studentForm=studentForm(request.POST)
        var_studentAddForm=studentAddForm(request.POST)
        if var_studentForm.is_valid() and var_studentAddForm.is_valid():
            studentprimary=var_studentForm.save()
            studentprimary.set_password(studentprimary.password)
            studentprimary.save()
            studentAdd=var_studentAddForm.save(commit=False)
            studentAdd.student=studentprimary
            studentAdd.save()
            registered=True
    else:
        var_studentForm=studentForm()
        var_studentAddForm=studentAddForm()
    return render(request,'gradesApp/registerStudent.html',{'var_studentForm':var_studentForm,'var_studentAddForm':var_studentAddForm,'registered':registered})


def registerTeacher(request):
    registered=False
    if request.method=='POST':
        var_teacherForm=teacherForm(request.POST)
        var_teacherAddForm=teacherAddForm(request.POST)
        if var_teacherForm.is_valid() and var_teacherAddForm.is_valid():
            teacherprimary=var_teacherForm.save()
            teacherprimary.set_password(teacherprimary.password)
            teacherprimary.save()
            teacherAdd=var_teacherAddForm.save(commit=False)
            teacherAdd.teacher=teacherprimary
            teacherAdd.save()
            registered=True
    else:
        var_teacherForm=teacherForm()
        var_teacherAddForm=teacherAddForm()
    return render(request,'gradesApp/registerTeacher.html',{'var_teacherForm':var_teacherForm,'var_teacherAddForm':var_teacherAddForm,'registered':registered})
    
def userLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin=True
            return redirect('/gradesApp/login/')
    else:
        return render(request,'gradesApp/login.html',{'invalidlogin':invalidlogin})

@login_required
def dashboard(request):
    try:
        current=Student.objects.get(student=request.user)
    except Student.DoesNotExist:
        current=Teacher.objects.get(teacher=request.user)
    if current.is_student:
        return redirect('/studentDash/')
    else:
        return redirect('/teacherDash/')
    return render(request,'gradesApp/dashboard.html')

    

def studentDash(request):
    return render(request,'gradesApp/studentDash.html')

def teacherDash(request):
    return render(request,'gradesApp/teacherDash.html')
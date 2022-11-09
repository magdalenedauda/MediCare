from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(req):
    return render(req, 'home.html')


def about(req):
    return render(req, 'about.html')


def contact(req):
    return render(req, 'contact.html')


def doctors(req):
    return render(req, 'doctors.html')

def appointment(req):
    return render(req, 'appointment.html')

def new_patient(req):
    return render(req, 'new_patient.html')

def dr_magdalene(req):
    return render(req, 'dr_magdalene.html')

def login(req):
    context = {}
     
    return render(req, 'login.html', context)

def sign_up(req):
    form = UserCreationForm()

    if req.method =='POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'account successfully created')
            return redirect('login')

    context = {'form':form}
    return render(req, 'sign_up.html', context)

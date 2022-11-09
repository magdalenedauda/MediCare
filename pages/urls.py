from django.urls import path
from .views import *

urlpatterns = [
        path('', home, name="home"),
        path('about/', about, name="about"),
        path('contact/', contact, name="contact"),
        path('doctors/', doctors, name="doctors"),
        path('appointment/', appointment, name="appointment"),
        path('new_patient/', new_patient, name="new_patient"),
        path('dr_magdalene/', dr_magdalene, name="dr_magdalene"),
        path('login/', login, name="login"),
        path('sign_up/', sign_up, name="signup")
]
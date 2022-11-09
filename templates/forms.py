from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import user
from django import form


class CreateUserForm(UserCreationForm):
    class meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
from django.forms import ModelForm
from . models import Task, Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms

from django.contrib.auth.models import User
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LogInUserForm(AuthenticationForm):

    username = forms.CharField(widget = TextInput())
    password = forms.CharField(widget = PasswordInput())

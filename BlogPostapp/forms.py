from django.forms import ModelForm
from .models import Blog
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput,TextInput
from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2']
       

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model= Blog
        fields='__all__'
        
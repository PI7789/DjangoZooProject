from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ZooUser

from django import forms
from django.forms.widgets import PasswordInput, TextInput

# register or create user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']


# login user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ZooUser
        fields = ['username', 'phonenum', 'email', 'points']
        
        #need to add a readonly widget

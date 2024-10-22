from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm 

# Create your views here.

def homepage(request):
    return render(request, 'pages/index.html')

def register(request):
    form = CreateUserForm()
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm 
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(request, 'pages/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created")
            return redirect('')

    context = {'form': form}

    return render (request,'pages/register.html', context=context)

def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            messages.success(request, "Successfully logged in")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('')
    
    context = {'login_form': form}
    return render(request,'pages/login.html', context=context)
@login_required(login_url="login")
def profile(request):
    username = request.user.username  # Get the username 
    return render(request, 'pages/profile.html', {'username': username})

def logout(request):

    auth.logout(request)
    messages.success(request, "Logged out")
    return redirect('')

def animalpage(request):
    return render(request, 'pages/animals.html')

def hotelinfo(request):
    return render(request, 'pages/hotel.html')
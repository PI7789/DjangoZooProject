from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, ProfileForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ZooUser


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
def updateprofile(request):
    form = ProfileForm()
    username = request.user.username  # Get the username 
    if request.method == "POST":
        form = ProfileForm(request, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "profile")
            return redirect('profile')
    context = {'ProfileForm': form , 
               'username' : username} 
    return render(request, 'pages/profileupdate.html', context=context)

def logout(request):

    auth.logout(request)
    messages.success(request, "Logged out")
    return redirect('')

def animalpage(request):
    return render(request, 'pages/animals.html')

def hotelinfo(request):
    return render(request, 'pages/hotel.html')

@login_required(login_url='login')
def profile(request, pk):
    print("WORKS")

    one_record = ZooUser.object.get(id=pk)
    context = {'record':one_record}
    return render(request, 'website/view-record.html', context = context)



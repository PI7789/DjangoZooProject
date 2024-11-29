from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, ProfileForm, Hotel_Booking_Form, PaymentForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ZooUser, HotelBooking



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
def updateprofile(request, pk):
    
    one_record = ZooUser.objects.get(id=pk)
    form = ProfileForm(instance=one_record)
    username = request.user.username  # Get the username 
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=one_record)
        if form.is_valid():
            form.save()
            return redirect('profile', pk)
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
     one_record = ZooUser.objects.get(id=pk)
     context = {'record':one_record}     
     return render(request, 'pages/profile.html', context = context)
@login_required(login_url='login')
def delete_account(request, pk):
    record = ZooUser.objects.get(id=pk)
    record.delete()

    return redirect("")

def delconfirmation(request):
    return render(request, 'pages/deleteconfirmation.html')


@login_required(login_url="login")
def booking (request):

    form = Hotel_Booking_Form()

    if request.method == "POST":
        print("on booking")
        updated_request = request.POST.copy()
        updated_request.update({'hotel_user_id_id': request.user})

        form = Hotel_Booking_Form(updated_request)
       

        if form.is_valid():
            obj = form.save(commit=False)

            arrive = obj.hotel_booking_date_arrive
            depart = obj.hotel_booking_date_leave
            result = depart - arrive


            hotel_total_cost = int(obj.hotel_booking_adults) * 65 \
            + int(obj.hotel_booking_children) * 35 \
            + int(obj.hotel_booking_oap) * 45
            hotel_total_cost *= int(result.days)

            hotel_points = int(hotel_total_cost)



            obj.hotel_points = hotel_points
            obj.hotel_total_cost = hotel_total_cost
            obj.hotel_user_id = request.user

            obj.save()

           

            messages.success(request, "Hotel Booked Successfully")
            return redirect('Payment') 


        else:
             print("there was a problem with the form")
             return redirect('hotel')
    context = {'form': form}

    return render(request, 'pages/booking1.html', context=context, )  


@login_required(login_url="login")
def Payment(request):
    one_record = ZooUser.objects.get(id=request.user.id)
    booking = HotelBooking.objects.latest("hotel_user_id")
    form = PaymentForm()

    if request.method == "POST":
        
            print("paymeent accepted")
            updated_request = request.POST.copy()
            updated_request.update({'hotel_user_id_id': request.user})

            form = PaymentForm(updated_request)

            if form.is_valid():
                obj = form.save(commit=False)




                obj.save()
                cpoints = request.POST.get("use_points")
                
                request.user.addpoints(booking.hotel_points)
                checkbox_points =  request.POST.get("use_points")
                if checkbox_points == "yes":
                    request.user.spendpoints(booking.hotel_total_cost)


                messages.success(request, "Payment Successful")

                return redirect('')   
            else:
                print("there was a problem with the Payment")
                return redirect('')
        
    context = {'paymentform': form, 
               'booking': booking}
    return render(request, 'pages/Payment.html', context = context)


def Loyalty(request):
    if request.user.is_authenticated:
        one_record = ZooUser.objects.get(id=request.user.id)
    return render(request, 'pages/loyalty.html')

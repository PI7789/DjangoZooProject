from django.urls import path
from . import views
urlpatterns = [


    path('', views.homepage, name = ''),

    path('register', views.register, name="register"),

    path('login', views.login, name="login"),

    path('profile/<int:pk>', views.profile, name = "profile"),

    path('updateprofile/<int:pk>', views.updateprofile, name = "updateprofile"),

    path('logout', views.logout, name= "logout"),

    path('animals', views.animalpage, name = "animals"),

    path('hotel', views.hotelinfo, name = "hotel"),

    path('delete-account/<int:pk>', views.delete_account, name="delete-account"),
]


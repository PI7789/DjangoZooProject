from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class ZooUser(AbstractUser):
    phonenum = models.CharField(max_length=14, blank=True)
    points = models.IntegerField(default = 0)

    def addpoints(self, cost):
        self.points += cost // 10

        self.save()

    def spendpoints(self, cost):
        
        if self.points < cost:
            self.points = 0
        else:
            self.points - cost
        self.save()


        return cost
    


        
class HotelBooking(models.Model):

    booking_id = models.AutoField(primary_key=True, editable = False)
    hotel_user_id = models.ForeignKey(ZooUser, on_delete=models.CASCADE)
    hotel_booking_date = models.DateField(auto_now_add=True)
    hotel_booking_date_arrive = models.DateField()
    hotel_booking_date_leave = models.DateField()
    hotel_booking_adults = models.IntegerField(default=0)
    hotel_booking_children = models.IntegerField(default=0)
    hotel_booking_oap = models.IntegerField(default=0)
    hotel_total_cost = models.FloatField(default=0)
    hotel_points = models.IntegerField(default=0)

class PaymentModel(models.Model):
    card_num = models.CharField(max_length=16, blank=True)
    Expiry_Date = models.CharField(max_length=5, blank=True)
    Card_Name = models.CharField(max_length=40, blank=True)
    security_code = models.CharField(max_length=3, blank=True)
from django.db import models

from apps.hotel_admin.CommonChoice import HotelBookingStatus, AccountStatus


class Hotel(models.Model):
    hotel_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=200, null=True)
    about = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    alternative_mobile = models.CharField(max_length=20)
    email = models.EmailField(null=True,max_length=50, unique=True)
    alternative_email = models.EmailField(null=True, max_length=50, unique=True)
    established = models.DateField(null=True, blank=True)
    booking_status = models.CharField(null=True, max_length=10, choices=HotelBookingStatus.choices,
        default=HotelBookingStatus.OPEN)
    status = models.CharField(null=True, max_length=10, choices=AccountStatus.choices,
                                      default=AccountStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "hotels"
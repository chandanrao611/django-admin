from django.db import models
from apps.customers.models import Customer
from apps.hotel_admin.CommonChoice import BookingStatus


class Booking(models.Model):
    booking_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    check_in = models.DateField()
    check_out = models.DateField()
    gst = models.DecimalField(max_digits=10, decimal_places=2)
    cgst = models.DecimalField(max_digits=10, decimal_places=2)
    sgst = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_status = models.CharField(
        max_length=20,
        choices=BookingStatus.choices,
        default=BookingStatus.BOOKED,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.total_amount}"

    class Meta:
        db_table = "bookings"
from django.db import models
from apps.hotel_admin.CommonChoice import RoomStatus, RoomType
from apps.hotels.models import Hotel


class Room(models.Model):
    room_id = models.BigAutoField(primary_key=True)
    room_number = models.CharField(max_length=20,unique=False)
    room_type = models.CharField(max_length=20, choices=RoomType.choices, default=RoomType.SINGLE)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    max_capacity = models.IntegerField(default=1)
    floor = models.IntegerField()
    status = models.CharField(max_length=20, choices=RoomStatus.choices, default=RoomStatus.AVAILABLE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name="rooms",
        null = True
    )

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"

    class Meta:
        db_table = "rooms"
from django.db import models

class Gender(models.TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"
    OTHER = "other", "Other"

class RoomStatus(models.TextChoices):
    AVAILABLE = "available", "Available"
    BOOKED = "booked", "Booked"
    MAINTENANCE = "maintenance", "Maintenance"


class RoomType(models.TextChoices):
    SINGLE = "single", "Single"
    DOUBLE = "double", "Double"
    DELUXE = "deluxe", "Deluxe"
    SUITE = "suite", "Suite"

class BookingStatus(models.TextChoices):
    BOOKED = "booked", "Booked"
    CONFIRM = "confirm", "Confirm"
    REJECT = "reject", "Reject"
    PENDING = "pending", "Booking Pending"

class AccountStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    ACTIVE = "active", "Active"
    INACTIVE = "inactive", "Inactive"

class HotelBookingStatus(models.TextChoices):
    OPEN = "open", "Open"
    CLOSE = "close", "Close"
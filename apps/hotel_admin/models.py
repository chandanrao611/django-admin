from django.contrib.auth.models import AbstractUser
from django.db import models
from .GenderChoice import Gender

class AdminUser(AbstractUser):
    mobile = models.BigIntegerField(default=0)
    profile_picture = models.CharField(null=True,max_length=10, blank=False)
    address = models.TextField(null=True,blank=True)
    email = models.EmailField(null=True,max_length=50, unique=True)
    dob = models.DateField(null=True)
    gender = models.CharField(
        null=True,
        max_length=10,
        choices=Gender.choices,
        default=Gender.MALE,
    )
    city = models.CharField(null=True,max_length=50)
    district = models.CharField(null=True,max_length=50)
    state = models.CharField(null=True,max_length=50)
    pincode = models.CharField(null=True,max_length=10)
    status = models.CharField(null=True,max_length=10, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    class Meta:
        db_table = "auth_user"
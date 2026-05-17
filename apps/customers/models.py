from django.db import models
from apps.hotel_admin.CommonChoice import Gender

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField("First Name", max_length=255)
    last_name = models.CharField("Last Name", max_length=255)
    email = models.EmailField(null=True, max_length=50, unique=True)
    mobile = models.BigIntegerField(default=0, unique=True)
    password = models.CharField("Password", max_length=255)
    profile_picture = models.CharField(null=True,max_length=10, blank=False)
    address = models.TextField(null=True,blank=True)
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
    pincode = models.CharField(null=True,max_length=6)
    status = models.CharField(null=True,max_length=10, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.customer_id)}"

    class Meta:
        db_table = "customers"
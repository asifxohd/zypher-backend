from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model for handling different types of users.
    """
    PHONE_NUMBER_LENGTH = 10
    ROLE_CHOICES = (
        ('investor', 'Investor'),
        ('startup', 'Startup'),
        ('admin', 'Admin'),
    )
                     
    phone_number = models.CharField(max_length=PHONE_NUMBER_LENGTH, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=300, unique=True)

    def __str__(self):
        """ String representation of the CustomUser instance """
        return self.username

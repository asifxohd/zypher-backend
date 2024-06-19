"""imports"""
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
    DEFAULT_ROLE = 'admin'
                     
    phone_number = models.CharField(max_length=PHONE_NUMBER_LENGTH, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=DEFAULT_ROLE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=300, unique=True)
    status = models.BooleanField(default=True)

def __str__(self) -> str:
    """String representation of the CustomUser instance."""
    return self.username



class Location(models.Model):
    """
    Model representing a location.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self)-> str:
        return f'{self.name}'


class Industry(models.Model):
    """
    Model representing an industry.
    """
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self)-> str:
        return f'{self.name}'



class InvestorPreferences(models.Model):
    """
    Model representing investor preferences.
    """
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='preferences')
    preferred_locations = models.ManyToManyField(Location)
    preferred_industries = models.ManyToManyField(Industry)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True) 
    def __str__(self)-> str:
        return f'{self.user_id}'


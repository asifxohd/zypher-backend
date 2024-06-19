""" imports """
from django.db import models
from userAuthentications.models import CustomUser

class StartupInformation(models.Model):
    """ 
        Table for storing information About the Business
    """
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    website_url = models.URLField()
    business_type = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    company_stage = models.CharField(max_length=100)
    annual_revenue = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    seeking_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    employee_count = models.PositiveIntegerField()
    linkedin_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    description = models.TextField()
    contact_number = models.CharField(max_length=12,  null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.title}'

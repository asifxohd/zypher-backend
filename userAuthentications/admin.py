from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(Industry)
admin.site.register(Location)
admin.site.register(InvestorPreferences)
admin.site.register(CustomUser)
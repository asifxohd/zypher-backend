from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *


router = DefaultRouter()
router.register(r'business/', BusinessProfileManager)

urlpatterns = [
    path('', include(router.urls)),
    path('investors/<str:user_id>/', GetInvestorProfile.as_view(), name='get-investor-details'),
    

]

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('get-investors/', InvestorUser.as_view(), name='get-investors'),
    path('change-status-investors/', InvestorUser.as_view(), name='block-investors'),
    path('get-investor-info/', InvestorInfoAPIView.as_view(), name='get_investor_info'),
    path('get-startups/', StartupUser.as_view(), name='get_investor_info'),
    path('change-status/', StartupUser.as_view(), name='block-investors'),
    path('get-startups-info/', StartupInfoAPIView.as_view(), name='search_startup'),

]

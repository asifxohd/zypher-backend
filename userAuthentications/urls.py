from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('verify/otp/', OTPVerificationView.as_view(), name='verify_otp'),
    path('resend/otp/', ResendOtpView.as_view(), name='resend_otp'),
    path('getlocationandindustry/', IndustryAndLocation.as_view(), name='industry_and_location'),
    path('saveIndustryandLocationInvestor', SaveInvestorPreferences.as_view(), name='save_industryand_location'),
    path('googleauthvalidation/', GoogleAuthVerificationRequest.as_view(), name='googleValidation'),
    path('checkuser/', CheckUserForGoogleAuth.as_view(), name='checkuser')
]

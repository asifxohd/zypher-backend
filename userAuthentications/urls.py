from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, OTPVerificationView, ResendOtpView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('verify/otp/', OTPVerificationView.as_view(), name='verify_otp'),
    path('resend/otp/', ResendOtpView.as_view(), name='resend_otp'),
]

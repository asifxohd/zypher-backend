"""Imports"""
import json
import random
from datetime import datetime, timedelta
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.conf import settings
from twilio.rest import Client
from django_redis import get_redis_connection
from .models import CustomUser
from .serializer import UserSerializer, OTPSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Handles user registration."""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class MessageHandler:
    """Handles sending OTP messages."""
    phone_number = None
    otp = None
    
    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp
    
    def send_otp_via_message(self):     
        """Send OTP via SMS."""
        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
        message = client.messages.create(body=f'Your One Time OTP For Zephyr Registrations is: {self.otp}. Do not share this OTP with anyone',
                                        from_=f'{settings.TWILIO_PHONE_NUMBER}',
                                        to=f'{settings.COUNTRY_CODE}{self.phone_number}')

class OTPVerificationView(APIView):
    """Handles OTP verification."""
    def post(self, request):
        """POST method to verify OTP."""
        otp_serializer = OTPSerializer(data=request.data)
        if otp_serializer.is_valid():
            phone_number = otp_serializer.validated_data['phone_number']
            input_otp = request.data.get('otp')
            redis_connection = get_redis_connection("default")
            data_json = redis_connection.get(phone_number)
            if data_json is not None:
                user_data = json.loads(data_json)
                if input_otp == str(user_data['otp']):
                    current_time = datetime.now()
                    otp_generated_time_str = user_data['otp_generated_time']
                    otp_generated_time_str_with_date = f"{current_time.date()} {otp_generated_time_str}"
                    otp_generated_time = datetime.strptime(otp_generated_time_str_with_date, "%Y-%m-%d %H:%M:%S")
                    time_difference = current_time - otp_generated_time
                    if time_difference <= timedelta(seconds=80):
                        user_data.pop('otp', None)
                        user_data.pop('otp_generated_time', None)
                        CustomUser.objects.create_user(**user_data)
                        redis_connection.delete(phone_number)
                        print("OTP successfully validated")
                        return Response({"message": "OTP successfully validated"}, status=status.HTTP_200_OK)
                    else:
                        return Response({"message": "OTP validation timeout"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"message": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                message = "Something went wrong. Please restart the registration process."
                return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"message": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)


class ResendOtpView(APIView):
    """ Handles OTP Resending """
    def post(self, request):
        """POST method to resend OTP."""
        print(request.data)
        phone_number = request.data.get('phone_number')
        print(phone_number)
        current_time = datetime.now()
        redis_connection = get_redis_connection("default")
        
        if redis_connection.exists(phone_number):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            data_json = redis_connection.get(phone_number)
            user_data = json.loads(data_json)
            
            new_otp = random.randint(100000, 999999)
            
            user_data['otp'] = new_otp
            user_data['otp_generated_time'] = current_time.strftime("%H:%M:%S")
            
            redis_connection.set(phone_number, json.dumps(user_data))
            message_handler = MessageHandler(phone_number, new_otp)
            try:
                message_handler.send_otp_via_message()
            except Exception as e:
                print("Error while sending OTP via message handler, try again: ", e)
            
            return Response({"message": "OTP resent successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Retry the registration process"}, status=status.HTTP_400_BAD_REQUEST)

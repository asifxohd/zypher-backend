"""Imports"""
import random
import json
from datetime import datetime
from django_redis import get_redis_connection
from rest_framework import serializers
from .models import CustomUser



class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User objects.
    """

    class Meta:
        """
        Handling model information while registering users.
        """
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone_number', 'role', 'full_name']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        """
        Custom method to save user data in Redis.
        """
        from .views import MessageHandler
        
        redis_connection = get_redis_connection("default")
        validated_data = dict(self.validated_data)
        otp = random.randint(100000, 999999)
        validated_data['otp'] = otp
        current_time = datetime.now()
        validated_data['otp_generated_time'] = current_time.strftime("%H:%M:%S")
        validated_data_json = json.dumps(validated_data)
        print(validated_data_json)
        redis_connection.setex(validated_data['phone_number'], 1800, validated_data_json)
        message_handler = MessageHandler(validated_data['phone_number'], otp)
        try:
            message_handler.send_otp_via_message()
        except Exception as e:
            print("error while sending OTP via message handler, try again: ", e)
        
        return validated_data

    
    
class OTPSerializer(serializers.Serializer):
    """
    Serializer for validating OTP (One-Time Password) data.

    Attributes:
        phone_number (str): The phone number associated with the OTP.
        otp (str): The OTP code to be validated, typically a 6-digit code.
    """

    phone_number = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)

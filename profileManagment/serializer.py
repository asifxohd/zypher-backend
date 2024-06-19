from rest_framework import serializers
from userAuthentications.models import CustomUser, InvestorPreferences, Location, Industry
from .models import StartupInformation

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['id', 'name']

class InvestorPreferencesSerializer(serializers.ModelSerializer):
    preferred_locations = serializers.SerializerMethodField()
    preferred_industries = serializers.SerializerMethodField()

    class Meta:
        model = InvestorPreferences
        fields = ['id', 'description', 'image', 'user_id', 'preferred_locations', 'preferred_industries']

    def get_preferred_locations(self, obj):
        return LocationSerializer(obj.preferred_locations.all(), many=True).data

    def get_preferred_industries(self, obj):
        return IndustrySerializer(obj.preferred_industries.all(), many=True).data

class CustomUserSerializer(serializers.ModelSerializer):
    preferences = InvestorPreferencesSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'full_name', 'phone_number', 'role', 'status', 'preferences']
        
class StartUpInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupInformation
        fields = '__all__' 

# Django imports
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Importing models and serializers from the application
from userAuthentications.models import CustomUser
from .serializer import CustomUserSerializer, StartUpInformationSerializer
from .models import StartupInformation


class GetInvestorProfile(APIView):
    """
    API endpoint for retrieving an individual investor's profile data.
    """

    def get(self, request, user_id):
        """
        Retrieves an individual investor's profile data.

        Args:
            request: HTTP request object.
            user_id: ID of the investor user.

        Returns:
            Serialized data containing user details and preferences.
        """
        investor_user = get_object_or_404(CustomUser, id=user_id, role='investor')
        investor_user_serializer = CustomUserSerializer(investor_user)
        # print(investor_user_serializer.data)
        
        return Response({
            'user_details': investor_user_serializer.data,
        })
        
        
class BusinessProfileManager(viewsets.ModelViewSet):
    queryset = StartupInformation.objects.all()
    serializer_class = StartUpInformationSerializer
    permission_classes=[IsAuthenticated]

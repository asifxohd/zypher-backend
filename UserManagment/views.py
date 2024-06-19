from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userAuthentications.models import CustomUser
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from userAuthentications.utiles import IsAdmin


class CustomPagination(PageNumberPagination):
    """
    Custom pagination class for handling paginated responses.

    Attributes:
        page_size (int): The default number of items to include on each page.
        page_size_query_param (str): The query parameter name for specifying the page size.
        max_page_size (int): The maximum allowed page size to prevent excessive resource consumption.
    """

    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100



class InvestorUser(APIView):
    """
    API endpoint for handling investor user related operations.
    """
    
    pagination_class = CustomPagination
    permission_classes=[IsAuthenticated, IsAdmin]
    
    def get(self, request):
        """
        Handle GET request for retrieving investor user information.

        Parameters:
        - request (HttpRequest): The HTTP request object.

        Returns:
        - Response: HTTP response object with investor user information.
        """
        try:
            investor_users = CustomUser.objects.filter(role='investor')
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        sorted_investor_users = sorted(investor_users, key=lambda x: x.id)

        # Paginate the queryset
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(sorted_investor_users, request)

        investor_user_data = []
        for investor_user in result_page:
            investor_user_data.append({
                'id': investor_user.id,
                'phone_number': investor_user.phone_number,
                'full_name': investor_user.full_name,
                'email': investor_user.email,
                'status': investor_user.status
            })
            
        return paginator.get_paginated_response(investor_user_data)
    
    def patch(self, request):
        """
        Handle PATCH request for blocking/unblocking investor user.

        Parameters:
        - request (HttpRequest): The HTTP request object.

        Returns:
        - Response: HTTP response object indicating the success of the operation.
        """
        try:
            user_id = request.data.get('id')
            user = CustomUser.objects.get(id=user_id)
            user.status = not user.status
            user.save()
            return Response(data={'success': True}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response(data={'success': False, 'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(data={'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
class InvestorInfoAPIView(APIView):
    """
    API endpoint to retrieve investor information based on search query.
    """
    
    permission_classes=[IsAuthenticated, IsAdmin]

    def get(self, request, format=None):
        """
        Handle GET request to retrieve investor information.

        Args:
            request (Request): The request object.
            format (str, optional): The requested format.

        Returns:
            Response: A JSON response containing the serialized investor data.
        """
        search_query = request.query_params.get('search', '')

        if search_query:
            investors = CustomUser.objects.filter(
                Q(phone_number__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(full_name__icontains=search_query),
                role='investor'
            )
            sorted_investors = investors.order_by('full_name')
            serialized_investors = list(sorted_investors.values('id', 'full_name', 'email', 'phone_number', 'role', 'status'))
            return Response(serialized_investors, status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_200_OK)  
        
        
class StartupUser(APIView):
    """
    API endpoint for handling startup user related operations.
    """
    
    pagination_class = CustomPagination
    permission_classes=[IsAuthenticated, IsAdmin]
    
    def get(self, request):
        """
        Handle GET request for retrieving startup user information.

        Parameters:
        - request (HttpRequest): The HTTP request object.

        Returns:
        - Response: HTTP response object with startup user information.
        """
        try:
            startup_users = CustomUser.objects.filter(role='startup')
            print(startup_users.count())
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        sorted_startup_users = sorted(startup_users, key=lambda x: x.id)

        # Paginate the queryset
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(sorted_startup_users, request)

        startup_user_data = []
        for startup_user in result_page:
            startup_user_data.append({
                'id': startup_user.id,
                'phone_number': startup_user.phone_number,
                'full_name': startup_user.full_name,
                'email': startup_user.email,
                'status': startup_user.status
            })
            
        return paginator.get_paginated_response(startup_user_data)
    
    def patch(self, request):
        """
        Handle PATCH request for blocking/unblocking investor user.

        Parameters:
        - request (HttpRequest): The HTTP request object.

        Returns:
        - Response: HTTP response object indicating the success of the operation.
        """
        try:
            user_id = request.data.get('id')
            user = CustomUser.objects.get(id=user_id)
            user.status = not user.status
            user.save()
            return Response(data={'success': True}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response(data={'success': False, 'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(data={'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class StartupInfoAPIView(APIView):
    """
    API endpoint to retrieve startup information based on search query.
    """
    
    permission_classes=[IsAuthenticated, IsAdmin]

    def get(self, request, format=None):
        """
        Handle GET request to retrieve startup information.

        Args:
            request (Request): The request object.
            format (str, optional): The requested format.

        Returns:
            Response: A JSON response containing the serialized startup data.
        """
        search_query = request.query_params.get('search', '')

        if search_query:
            startups = CustomUser.objects.filter(
                Q(phone_number__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(full_name__icontains=search_query),
                role='startup'
            )
            sorted_startups = startups.order_by('full_name')
            serialized_startups = list(sorted_startups.values('id', 'full_name', 'email', 'phone_number', 'role', 'status'))
            return Response(serialized_startups, status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_200_OK)  
        
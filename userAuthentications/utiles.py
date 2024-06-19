""" imports """
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Permission class to check if the user is an admin.
    """

    def has_permission(self, request, view):
        """
        Check if the user has admin role.

        Parameters:
        - request: Django HttpRequest object.
        - view: DRF View object.

        Returns:
        - Boolean indicating whether the user is an admin or not.
        """
        return request.user and request.user.role == 'admin'
    
class IsInvestor(BasePermission):
    """
    Permission class to check if the user is an investor.
    """

    def has_permission(self, request, view):
        """
        Check if the user has investor role.

        Parameters:
        - request: Django HttpRequest object.
        - view: DRF View object.

        Returns:
        - Boolean indicating whether the user is an investor or not.
        """
        return request.user and request.user.role == 'investor'
    
class IsStartup(BasePermission):
    """
    Permission class to check if the user is a startup.
    """

    def has_permission(self, request, view):
        """
        Check if the user has startup role.

        Parameters:
        - request: Django HttpRequest object.
        - view: DRF View object.

        Returns:
        - Boolean indicating whether the user is a startup or not.
        """
        return request.user and request.user.role == 'startup'

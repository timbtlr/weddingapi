from django.conf import settings
from rest_framework.permissions import BasePermission
from rest_framework.authentication import get_authorization_header

class ViewModelPermissions(BasePermission):
    """
    Allows access only to authenticated users.
    """
    def has_permission(self, request, view):
    	if request.method == 'GET':
    		return True
    	else:
    		return request.user and request.user.is_authenticated()


class ApiTokenPermissions(BasePermission):
    """
    Allows access if the request contains a valid API key.
    """
    def has_permission(self, request, view):
    	key = get_authorization_header(request)
    	if key == settings.API_TOKEN:
    		return True
    	return False
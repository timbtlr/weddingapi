from rest_framework.permissions import BasePermission

class RsvpModelPermissions(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
    	print(dir(request.method ))

    	if request.method == 'POST' and request.user.is_authenticated():
    		return True
    	else:
    		return request.user.is_superuser
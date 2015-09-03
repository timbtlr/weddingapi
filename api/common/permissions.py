from rest_framework.permissions import BasePermission

class ViewModelPermissions(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
    	print(dir(request.method ))

    	if request.method == 'GET':
    		return True
    	else:
    		return request.user and request.user.is_authenticated()
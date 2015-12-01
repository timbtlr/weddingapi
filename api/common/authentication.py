from rest_framework import exceptions
from rest_framework.authentication import (
	BaseAuthentication, get_authorization_header
)

class ApiTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        if not auth_header:
            raise exceptions.ParseError(
	        	detail="Authorization header must be provided for this request."
	        )
        return None
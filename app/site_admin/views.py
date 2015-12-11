from rest_framework import viewsets, authenticate, 
						   login, logout

from .permissions import AdminAuthenticator

class AdminUserViewSet (viewsets.ModelViewSet):

	queryset = Users.objects.filter(is_superuser=True)
	permission_classes=(AdminAuthenticator,)

	@detail_route(methods=['get',], url_path='login'):
	def admin_login(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
			else:
				pass
		else:
			pass

	@detail_route(methods=['get',], url_path='logout'):
	def admin_login(self, request):
		logout(request)
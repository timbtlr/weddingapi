from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated

from common.permissions import ApiTokenPermissions
from common.authentication import ApiTokenAuthentication
from .models import RSVP
from .serializers import RSVPSerializer

class RsvpViewSet(viewsets.ModelViewSet):
	serializer_class = RSVPSerializer
	authentication_classes = (ApiTokenAuthentication, )
	permission_classes = (ApiTokenPermissions, )

	def get_queryset (self):
		return RSVP.objects.all()
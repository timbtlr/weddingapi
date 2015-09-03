from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated

from .models import RSVP
from .serializers import RSVPSerializer
from .permissions import RsvpModelPermissions

class RsvpViewSet(viewsets.ModelViewSet):
	serializer_class=RSVPSerializer
	permission_classes=(RsvpModelPermissions,)

	def get_queryset (self):
		return RSVP.objects.all()
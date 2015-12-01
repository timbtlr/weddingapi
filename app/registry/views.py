from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import detail_route

from .models import RegistryItem
from .serializers import RegistryItemSerializer

class RegistryItemViewSet(viewsets.ModelViewSet):

	serializer_class=RegistryItemSerializer

	def get_queryset (self):
		return RegistryItem.objects.all()

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.mixins import ListModelMixin

from .models import Photo
from .serializers import PhotoSerializer

class PhotoViewSet(viewsets.ModelViewSet):
	serializer_class=PhotoSerializer

	def get_queryset (self):
		return Photo.objects.all()
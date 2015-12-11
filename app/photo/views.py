from rest_framework import viewsets
from rest_condition import Or
from common.permissions import ApiTokenPermissions, GetPermission
from .models import Photo
from .serializers import PhotoSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class=PhotoSerializer

    permission_classes = (Or(ApiTokenPermissions, GetPermission), )

    def get_queryset (self):
        return Photo.objects.all()
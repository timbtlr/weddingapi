from rest_framework import viewsets
from rest_condition import Or
from common.permissions import ApiTokenPermissions, GetPermission
from .models import RegistryItem
from .serializers import RegistryItemSerializer


class RegistryItemViewSet(viewsets.ModelViewSet):
    serializer_class = RegistryItemSerializer
    permission_classes = (Or(ApiTokenPermissions, GetPermission), )

    def get_queryset(self):
        return RegistryItem.objects.all()

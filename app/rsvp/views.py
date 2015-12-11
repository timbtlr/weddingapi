from rest_framework import viewsets
from rest_condition import Or
from common.permissions import ApiTokenPermissions, GetPermission
from .models import RSVP
from .serializers import RSVPSerializer

class RsvpViewSet(viewsets.ModelViewSet):
    serializer_class = RSVPSerializer
    permission_classes = (Or(ApiTokenPermissions, GetPermission), )

    def get_queryset (self):
        return RSVP.objects.all()
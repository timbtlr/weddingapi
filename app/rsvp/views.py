from rest_framework import viewsets
from rest_condition import Or
from common.permissions import ApiTokenPermissions, GetPermission
from .models import Invitation, Invitee
from .serializers import InvitationSerializer, InviteeSerializer


class InvitationViewSet(viewsets.ModelViewSet):
    serializer_class = InvitationSerializer
    permission_classes = (ApiTokenPermissions, )

    def get_queryset (self):
        return Invitation.objects.all()


class InviteeViewSet(viewsets.ModelViewSet):
    serializer_class = InviteeSerializer
    permission_classes = (ApiTokenPermissions, )

    def get_queryset (self):
        return Invitee.objects.all()
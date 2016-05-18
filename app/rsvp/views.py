from rest_framework import viewsets
from rest_condition import Or
from rest_framework import filters
from common.permissions import ApiTokenPermissions, GetPermission
from .models import Invitation, Invitee
from .serializers import InvitationSerializer, InviteeSerializer


class InvitationViewSet(viewsets.ModelViewSet):
    serializer_class = InvitationSerializer
    permission_classes = (ApiTokenPermissions, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('invitees__name', )

    def get_queryset (self):
        return Invitation.objects.all()


class InviteeViewSet(viewsets.ModelViewSet):
    serializer_class = InviteeSerializer
    permission_classes = (ApiTokenPermissions, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('attending', )

    def get_queryset (self):
        return Invitee.objects.all()
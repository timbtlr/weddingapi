import json
from rest_framework import serializers
from .models import Invitation, Invitee

class InvitationSerializer(serializers.ModelSerializer):

    invitees = serializers.StringRelatedField(many=True)

    class Meta:
        model = Invitation
        fields = ('id', 'message', 'invitees', )

class InviteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitee
        fields = ('invitation', 'name', 'attending', )
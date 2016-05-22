import json
from rest_framework import serializers
from datetime import datetime
from .models import Invitation, Invitee

class InvitationSerializer(serializers.ModelSerializer):
    invitees = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Invitation
        fields = ('id', 'invite_name', 'message', 'invitees', 'song_request', )

class InviteeSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.timestamp = datetime.now()
        instance.attending = validated_data.get('attending')
        instance.save()
        return instance


    class Meta:
        model = Invitee
        fields = ('id', 'invitation', 'name', 'attending', 'timestamp', )
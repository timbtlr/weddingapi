from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            'id', 'full_url', 'caption'
        )

    def create(self, validated_data):
        return Photo.objects.create(**validated_data)

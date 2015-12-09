from rest_framework import serializers
from .models import RegistryItem


class RegistryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistryItem
        fields = ('store_name', 'description', 'registry_url', 'thumbnail_url')

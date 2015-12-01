from rest_framework import serializers

from .models import RegistryItem

class RegistryItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegistryItem
		fields = ('id', 'name', 'full_url', 'description',
				  'price', 'store', 'bought')
from service.list_api.models import ListItem
from rest_framework import serializers

class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListItem
        fields = ['url', 'name', 'position', 'completed']
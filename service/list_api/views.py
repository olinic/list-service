from service.list_api.serializers import ListItemSerializer
from service.list_api.models import ListItem
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ListItems(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListItemSerializer
    
    def get(self, request, format=None):
        queryset = ListItem.objects.filter(user=request.user)
        return Response(queryset)

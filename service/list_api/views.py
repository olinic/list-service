from service.list_api.serializers import ListItemSerializer
from service.list_api.models import ListItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all().order_by('position')
    serializer_class = ListItemSerializer
#    permission_classes = [IsAuthenticated]

#    def get_queryset(self):
#        return ListItem.objects.filter(user=self.request.user).order_by('position')
    
#    def perform_create(self, serializer):
#        serializer.save(user=self.request.user)
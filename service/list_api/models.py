from django.db import models
from django.contrib.auth.models import User
import uuid

class ListItem(models.Model):
   id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
   name = models.CharField(max_length = 180)
   position = models.IntegerField(unique = True)
   completed = models.BooleanField(default = False)
   user = models.ForeignKey(User, on_delete = models.CASCADE)

   def __str__(self):
      return self.name
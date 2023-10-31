from django.test import TestCase
from service.list_api.models import ListItem

class TestApi(TestCase):
   @classmethod
   def setUpTestData(cls):
      ListItem.objects.create(position=1, name="check")

   def setUp(self):
      pass

   def test_fetch_list_items(self):
      response = self.client.get("/list-items/")
      self.assertEqual(200, response.status_code)
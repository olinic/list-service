from django.test import TestCase

class TestApi(TestCase):
   @classmethod
   def setUpTestData(cls):
      pass

   def setUp(self):
      pass

   def test_this_is_false(self):
      self.assertFalse(False)
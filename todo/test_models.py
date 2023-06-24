from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        # Create an item to test
        item = Item.objects.create(name='Test Todo Item')
        # Check that done is False by default
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        # Create an item to test
        item = Item.objects.create(name='Test Todo Item')
        # Check that the string representation of the item is the name
        self.assertEqual(str(item), 'Test Todo Item')
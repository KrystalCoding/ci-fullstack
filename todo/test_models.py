from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_ot_false(self):
        item = Item.objects.create(name='Test To-do Item')
        self.assertFalse(item.done)
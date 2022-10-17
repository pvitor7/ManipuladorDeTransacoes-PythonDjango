from rest_framework.test import APITestCase
from Store.models import Store

class StoreModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.store_obj1 = {"store": "Store 1", "owner": "Admin"}
        cls.store_obj2 = {"store": "Store 2", "owner": "Other Admin"}

        cls.store_1 = Store.objects.create(**cls.store_obj1)
        cls.store_2 = Store.objects.create(**cls.store_obj2)

    def test_store_fields(self):
        self.assertEqual(self.store_1.store, self.store_obj1["store"])
        self.assertEqual(self.store_1.owner, self.store_obj1["owner"])

    def test_store_max_length(self):
        expected = 128
        length = self.store_1._meta.get_field("store").max_length
        self.assertEqual(expected, length)

    def test_owner_max_length(self):
        expected = 128
        length = self.store_1._meta.get_field("owner").max_length
        self.assertEqual(expected, length)


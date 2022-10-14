import datetime
from rest_framework.test import APITestCase
from Store.models import Store
from ..models import Transaction
import ipdb

# ipdb.set_trace()
class TransactionModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.store_obj1 = {"store": "Store 1", "owner": "Admin"}
        cls.store_obj2 = {"store": "Store 2", "owner": "Other Admin"}
        
        cls.store_1 = Store.objects.create(**cls.store_obj1)
        store_pk_1 = Store.objects.get(store=cls.store_obj1["store"])
        
        
        cls.store_2 = Store.objects.create(**cls.store_obj2)
        store_pk_2 = Store.objects.get(store=cls.store_obj2["store"])

        cls.transaction_obj1 = {
            "type_transaction": 3,
            "date": datetime.date(2019, 3, 1),
            "hour": datetime.time(15, 34, 53),
            "value": "142,00",
            "cpf": "09620676017",
            "card": "4753****3153",
            "operation": "Saída",
            "store": store_pk_1,
        }

        cls.transaction_obj2 = {
            "type_transaction": 5,
            "date": datetime.date(2019, 3, 1),
            "hour": datetime.time(14, 56, 7),
            "value": "132,00",
            "cpf": "55641815063",
            "card": "3123****7687",
            "operation": "Entrada",
            "store": store_pk_2,
        }

        cls.transaction1 = Transaction.objects.create(**cls.transaction_obj1)
        cls.transaction2 = Transaction.objects.create(**cls.transaction_obj2)

    def test_transaction_fields(self):
        self.assertEqual(self.transaction1.type_transaction, self.transaction_obj1["type_transaction"])
        self.assertEqual(self.transaction1.date, self.transaction_obj1["date"])
        self.assertEqual(self.transaction1.hour, self.transaction_obj1["hour"])
        self.assertEqual(self.transaction1.value, self.transaction_obj1["value"])
        self.assertEqual(self.transaction1.cpf, self.transaction_obj1["cpf"])
        self.assertEqual(self.transaction1.card, self.transaction_obj1["card"])
        self.assertEqual(self.transaction1.operation, self.transaction_obj1["operation"])
        self.assertEqual(self.transaction1.store, self.transaction_obj1["store"])

    def test_value_max_length(self):
        expected = 20;
        length = self.transaction1._meta.get_field("value").max_length
        self.assertEqual(expected, length)
        
    def test_cpf_max_length(self):
        expected = 128;
        length = self.transaction1._meta.get_field("cpf").max_length
        self.assertEqual(expected, length)
        
    def test_card_max_length(self):
        expected = 128;
        length = self.transaction1._meta.get_field("card").max_length
        self.assertEqual(expected, length)
        
    def test_operation_max_length(self):
        expected = 10;
        length = self.transaction1._meta.get_field("operation").max_length
        self.assertEqual(expected, length)
        
        
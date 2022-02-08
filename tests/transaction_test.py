import unittest
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction(30.00, "Asda", "grocery", 5)

    def test_transaction_has_amount(self):
        self.assertEqual(30.00, self.transaction.amount)
    def test_transaction_has_merchant(self):
        self.assertEqual("Asda", self.transaction.merchant)
    def test_transaction_has_tag(self):
        self.assertEqual("grocery", self.transaction.tag)
    def test_transaction_has_id(self):
        self.assertEqual(5, self.transaction.id)

        
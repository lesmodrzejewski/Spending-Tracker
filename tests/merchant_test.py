import unittest
from models.merchant import Merchant

class TestMerchant(unittest.TestCase):
    def setUp(self):
        self.merchant = Merchant("Asda", 3)

    def test_merchant_has_name(self):
        self.assertEqual("Asda", self.merchant.name)
    def test_merchant_has_id(self):
        self.assertEqual(3, self.merchant.id)

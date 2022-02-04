import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction


merchant_1 = Merchant("Asda")
merchant_2 = Merchant("Screwfix")

tag_1 = Tag("grocery")
tag_2 = Tag("tool")


transaction_1 = Transaction(25)
transaction_2 = Transaction(100)

pdb.set_trace()
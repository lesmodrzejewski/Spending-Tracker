import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

# merchant_repository.delete_all()
# tag_repository.delete_all()
# transaction_repository.delete_all()

merchant_1 = Merchant("Asda")
m1 = merchant_repository.save(merchant_1)
m3 = merchant_repository.select_all()
merchant_2 = Merchant("Screwfix")
m2 = merchant_repository.save(merchant_2)

tag_1 = Tag("grocery")
t1 = tag_repository.save(tag_1)
t3 = tag_repository.select_all()
# t3 = tag_repository.select()
tag_2 = Tag("tool")
t2 = tag_repository.save(tag_2)

transaction_1 = Transaction(25.00, merchant_1, tag_1)
tr1 = transaction_repository.save(transaction_1)
tr3 = transaction_repository.select_all()
transaction_2 = Transaction(100.00, merchant_2, tag_2)
tr2 = transaction_repository.save(transaction_2)


pdb.set_trace()
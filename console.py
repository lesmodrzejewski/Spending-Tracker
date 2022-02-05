
from os import preadv
import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

merchant_1 = Merchant("Asda")
merchant_repository.save(merchant_1)
merchant_2 = Merchant("Screwfix")
merchant_repository.save(merchant_2)

tag_1 = Tag("grocery")
tag_repository.save(tag_1)
tag_2 = Tag("tool")
tag_repository.save(tag_2)

transaction_1 = Transaction(25, merchant_1, tag_1)
transaction_repository.save(transaction_1)
import pdb; pdb.set_trace()
transaction_2 = Transaction(100)
# t2 = transaction_repository.save(transaction_2)
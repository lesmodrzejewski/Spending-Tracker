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
tag_2 = Tag("tool")


transaction_1 = Transaction(25)
transaction_2 = Transaction(100)

pdb.set_trace()
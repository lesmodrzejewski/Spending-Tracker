from unittest import result
from db.run_sql import run_sql

from models.transaction import Transaction

import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save(transaction):
    sql = """
    INSERT INTO transactions (amount, merchant_id, tag_id)
    VALUES (%s, %s, %s) RETURNING *
    """
    values = [transaction.amount, transaction.merchant.id, transaction.tag.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

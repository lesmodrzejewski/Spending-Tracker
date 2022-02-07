from db.run_sql import run_sql
from models.merchant import Merchant

from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

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

def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        print(row)
        merchant = merchant_repository.select(row['merchant_id'])
        tag = tag_repository.select(row['tag_id'])
        transaction = Transaction(row['amount'], merchant, tag, row['id'])
        transactions.append(transaction)
    return transactions


# def delete_all():
#     sql = "DELETE FROM transactions"
#     run_sql(sql)




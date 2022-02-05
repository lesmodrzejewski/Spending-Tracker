from controllers.merchants_controller import merchants
from db.run_sql import run_sql

from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES (%s) RETURNING *"
    values = [merchant.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant

# create a function that retrieves information 
# about merchants from the database

def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)
    return merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE ID = '%s'"
    value = [id]
    result = run_sql(sql, value)

    if result is not None:
        merchant = Merchant(result['name'], result['id'])
    return merchant




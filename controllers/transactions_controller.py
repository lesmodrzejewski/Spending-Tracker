from flask import Flask, render_template, Blueprint, request, redirect

from models.merchant import Merchant
from models.transaction import Transaction
from models.tag import Tag

from repositories import merchant_repository
from repositories import tag_repository
from repositories import transaction_repository

transactions_blueprint = Blueprint('transactions', __name__)

# SHOW ALL TRANSACTIONS

@transactions_blueprint.route('/transactions')
def transactions():
    transactions = transaction_repository.select_all()
    sum = transaction_repository.sum_up(transactions)
    return render_template('transactions/index.html', transactions = transactions, sum = sum)

# ADD NEW TRANSACTION

@transactions_blueprint.route('/transactions/new')
def add_new_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new.html", merchants=merchants, tags=tags)

@transactions_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    amount = request.form['amount']
    merchant_id = request.form['merchant_id']
    tag_id = request.form['tag_id']
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    transaction = Transaction(amount, merchant, tag)
    transaction_repository.save(transaction)
    return redirect('/transactions')


import imp
from flask import Flask, render_template, Blueprint, request, redirect
from repositories import merchant_repository
from repositories import tag_repository
from repositories import transaction_repository

from models.transaction import Transaction

tasks_blueprint = Blueprint('tasks', __name__)

@tasks_blueprint.route('/transactions')
def transactions():
    return render_template('transactions/index.html')
from re import S
from flask import Flask, render_template, Blueprint, request, redirect
from models.merchant import Merchant

from repositories import merchant_repository

merchants_blueprint = Blueprint('merchants', __name__)

@merchants_blueprint.route('/merchants')
def merchants():
    merchants = merchant_repository.select_all()
    return render_template('merchants/index.html', merchants=merchants)

@merchants_blueprint.route("/merchants/new")
def add_new_merchant():
    return render_template("merchants/new.html")

@merchants_blueprint.route('/merchants', methods=['POST'])
def create_task():
    name = request.form['add-new-merchant-name']
    merchant = Merchant(name)
    merchant_repository.save(merchant)
    return redirect('/merchants')
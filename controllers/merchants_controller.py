from flask import Flask, render_template, Blueprint, request, redirect
from models.merchant import Merchant

from repositories import merchant_repository

merchants_blueprint = Blueprint('merchants', __name__)

# SHOW ALL MERCHANTS

@merchants_blueprint.route('/merchants')
def merchants():
    merchants = merchant_repository.select_all()
    return render_template('merchants/index.html', merchants=merchants)


# SHOW ONE MERCHANT

@merchants_blueprint.route("/merchants/<id>")
def show_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('/merchants/show.html', merchant = merchant)


# ADD NEW MERCHANT

@merchants_blueprint.route("/merchants/new")
def add_new_merchant():
    return render_template("merchants/new.html")

@merchants_blueprint.route('/merchants', methods=['POST'])
def create_task():
    name = request.form['add-new-merchant-name']
    merchant = Merchant(name)
    merchant_repository.save(merchant)
    return redirect('/merchants')

# EDIT MERCHANT

@merchants_blueprint.route("/merchants/<id>/edit")
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/edit.html', merchant=merchant)

@merchants_blueprint.route("/merchants/<id>", methods=['POST'])
def update_merchant(id):
    name = request.form['edit-merchant']
    merchant = Merchant(name, id)
    merchant_repository.update(merchant)
    return redirect('/merchants')




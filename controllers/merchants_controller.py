from flask import Flask, render_template, Blueprint, request, redirect

from models.merchant import Merchant

from repositories import merchant_repository

merchants_blueprint = Blueprint('merchants', __name__)

@merchants_blueprint.route('/merchants')
def select_all():
    merchants = merchant_repository.select_all()
    return render_template('merchants/index.html', merchants=merchants)
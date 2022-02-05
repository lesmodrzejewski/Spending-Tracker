from flask import Blueprint, Flask, render_template

from repositories import tag_repository

tags_blueprint = Blueprint('tags', __name__)

@tags_blueprint.route('/tags')
def tags():
    tags = tag_repository.select_all()
    return render_template('tags/index.html', tags = tags)

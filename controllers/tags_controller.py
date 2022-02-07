from flask import Blueprint, Flask, redirect, render_template, request
from models.tag import Tag

from repositories import tag_repository

tags_blueprint = Blueprint('tags', __name__)

@tags_blueprint.route('/tags')
def tags():
    tags = tag_repository.select_all()
    return render_template('tags/index.html', tags = tags)

@tags_blueprint.route("/tags/new")
def add_new_tag():
    return render_template("tags/new.html")

@tags_blueprint.route("/tags", methods=['POST'])
def create_tag():
    name = request.form['add-new-tag-name']
    tag = Tag(name)
    tag_repository.save(tag)
    return redirect('/tags')



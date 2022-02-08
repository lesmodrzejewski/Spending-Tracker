from crypt import methods
from flask import Blueprint, Flask, redirect, render_template, request
from controllers.merchants_controller import merchants
from models.tag import Tag

from repositories import tag_repository

tags_blueprint = Blueprint('tags', __name__)

@tags_blueprint.route('/tags')
def tags():
    tags = tag_repository.select_all()
    return render_template('tags/index.html', tags = tags)

# SHOW ONE TAG

@tags_blueprint.route("/tags/<id>")
def show_tags(id):
    tag = tag_repository.select(id)
    return render_template('/tags/show.html', tag=tag)

# ADD NEW TAG

@tags_blueprint.route("/tags/new")
def add_new_tag():
    return render_template("tags/new.html")

@tags_blueprint.route("/tags", methods=['POST'])
def create_tag():
    name = request.form['add-new-tag-name']
    tag = Tag(name)
    tag_repository.save(tag)
    return redirect('/tags')

# EDIT TAG

@tags_blueprint.route("/tags/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template('tags/edit.html', tag = tag)

@tags_blueprint.route("/tags/<id>", methods=['POST'])
def update_tag(id):
    name = request.form['edit-tag']
    tag = Tag(name, id)
    tag_repository.update(tag)
    return redirect('/tags')


from db.run_sql import run_sql
from models.merchant import Merchant

from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (name) VALUES (%s) RETURNING *"
    values = [tag.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id
    return tag


def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row['name'], row['id'])
        tags.append(tag)
    return tags

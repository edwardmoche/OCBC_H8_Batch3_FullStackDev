"""
This is the director module and supports all the ReST actions for the
Director collection
"""

from flask import make_response, abort
from config import db
from models import Director, DirectorSchema, Movie


def read_all():
    """
    This function responds to a request for /api/director
    with the complete lists of director
    :return:        json string of list of director
    """

    director = Director.query.order_by(Director.id).all()

    director_schema = DirectorSchema(many=True)
    data = director_schema.dump(director)
    return data

def read_one(id):
    """
    This function responds to a request for /api/director/{id}
    with one matching director from directors
    :param id:   Id of director to find
    :return:            director matching id
    """
    
    director = (
        Director.query.filter(Director.id == id)
        .outerjoin(Movie)
        .one_or_none()
    )

    if director is not None:

        director_schema = DirectorSchema()
        data = director_schema.dump(director)
        return data

    else:
        abort(404, f"Director not found for Id: {id}")

def read_one_name(name):
    """
    This function responds to a request for /api/director/{name}
    with one matching director from directors
    :param name:   name of director to find
    :return:            director matching id
    """
    
    director = (
        Director.query.filter(Director.name == name)
        .outerjoin(Movie)
        .one_or_none()
    )

    if director is not None:

        director_schema = DirectorSchema()
        data = director_schema.dump(director)
        return data

    else:
        abort(404, f"Director not found for Name: {name}")

def create(directors):
    """
    This function creates a new director in the directors structure
    based on the passed in director data
    :param director:  director to create in directors structure
    :return:        201 on success, 406 on director exists
    """
    id = directors.get("id")

    existing_id = (
        Director.query.filter(Director.id == id)
        .one_or_none()
    )

    if existing_id is None:

        schema = DirectorSchema()
        new_director = schema.load(directors, session=db.session)

        db.session.add(new_director)
        db.session.commit()

        data = schema.dump(new_director)

        return data, 201

    else:
        abort(409, f"Directors with id {id} already exists")

def update(id, directors):
    """
    This function updates an existing director in the directors structure
    :param id:   Id of the director to update in the directors structure
    :param director:      director to update
    :return:            updated director structure
    """
    update_id = Director.query.filter(
        Director.id == id
    ).one_or_none()

    if update_id is not None:

        schema = DirectorSchema()
        update = schema.load(directors, session=db.session)

        update.id = update_id.id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_id)

        return data, 200

    else:
        abort(404, f"Director not found for Id: {id}")

def delete(id):
    """
    This function deletes a director from the directors structure
    :param id:   Id of the director to delete
    :return:            200 on successful delete, 404 if not found
    """
    director = Director.query.filter(Director.id == id).one_or_none()

    if director is not None:
        db.session.delete(director)
        db.session.commit()
        return make_response(f"Director with id : {id} deleted", 200)

    else:
        abort(404, f"Director not found for Id: {id}")
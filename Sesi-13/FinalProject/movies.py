"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from config import db
from models import Director, Movie, MovieSchema


def read_all():
    """
    This function responds to a request for /api/people/movies
    with the complete list of movies, sorted by note timestamp

    :return:                json list of all movies for all people
    """
    movie = Movie.query.order_by(Movie.id).all()

    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movie)
    return data

# ini tanya
def read_one(director_id, id):
    """
    This function responds to a request for
    /api/people/{person_id}/movies/{note_id}
    with one matching note for the associated person

    :param person_id:       Id of person the note is related to
    :param note_id:         Id of the note
    :return:                json string of note contents
    """
    movie = (
        Movie.query.join(Director, Director.id == Movie.director_id)
        .filter(Director.id == director_id)
        .filter(Movie.id == id)
        .one_or_none()
    )

    if movie is not None:
        movie_schema = MovieSchema()
        data = movie_schema.dump(movie)
        return data

    else:
        abort(404, f"Movie not found for Id: {id}")

def read_one_name(director_id, original_title):
    """
    This function responds to a request for
    /api/people/{person_id}/movies/{note_id}
    with one matching note for the associated person

    :param person_id:       Id of person the note is related to
    :param note_id:         Id of the note
    :return:                json string of note contents
    """
    movie = (
        Movie.query.join(Director, Director.id == Movie.director_id)
        .filter(Director.id == director_id)
        .filter(Movie.original_title == original_title)
        .one_or_none()
    )

    if movie is not None:
        movie_schema = MovieSchema()
        data = movie_schema.dump(movie)
        return data

    else:
        abort(404, f"Movie {original_title} not found")

def create(director_id, movies):
    """
    This function creates a new note related to the passed in person id.

    :param person_id:       Id of the person the note is related to
    :param note:            The JSON containing the note data
    :return:                201 on success
    """
    director = Director.query.filter(Director.id == director_id).one_or_none()

    if director is None:
        abort(404, f"Director not found for Id: {director_id}")

    schema = MovieSchema()
    new_movie = schema.load(movies, session=db.session)

    # Add the note to the person and database
    director.movies.append(new_movie)
    db.session.commit()

    # Serialize and return the newly created note in the response
    data = schema.dump(new_movie)

    return data, 201

def update(director_id, id, movies):
    """
    This function updates an existing note related to the passed in
    person id.

    :param person_id:       Id of the person the note is related to
    :param note_id:         Id of the note to update
    :param content:            The JSON containing the note data
    :return:                200 on success
    """
    update_movie = (
        Movie.query.filter(Director.id == director_id)
        .filter(Movie.id == id)
        .one_or_none()
    )

    if update_movie is not None:

        schema = MovieSchema()
        update = schema.load(movies, session=db.session)

        update.person_id = update_movie.person_id
        update.note_id = update_movie.note_id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_movie)

        return data, 200

    else:
        abort(404, f"Note not found for Id: {id}")

def delete(director_id, id):
    """
    This function deletes a note from the note structure

    :param person_id:   Id of the person the note is related to
    :param note_id:     Id of the note to delete
    :return:            200 on successful delete, 404 if not found
    """
    movie = (
        Movie.query.filter(Director.id == director_id)
        .filter(Movie.id == id)
        .one_or_none()
    )

    if movie is not None:
        db.session.delete(movie)
        db.session.commit()
        return make_response(
            "Movie {id} deleted".format(id=id), 200
        )

    else:
        abort(404, f"Movie not found for Id: {id}")
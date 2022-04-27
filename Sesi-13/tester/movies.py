"""
This is the directors module and supports all the REST actions for the
directors data
"""

from flask import make_response, abort
from config import db
from models import Director, Movie, MovieSchema

class Movies:
    def read_all():
        """
        This function responds to a request for /api/directors/movies
        with the complete list of movies, sorted by movie id

        :return:                json list of all movies for all directors
        """
        
        movies = Movie.query.order_by(db.desc(Movie.movie_id)).limit(50).all()

        movie_schema = MovieSchema(many=True)
        data = movie_schema.dump(movies)
        return data


    def read_one(director_id, movie_id):
        """
        This function responds to a request for
        /api/directors/{director_id}/movies/{movie_id}
        with one matching movie for the associated director

        :param director_id:       Id of director the movie is related to
        :param movie_id:         Id of the movie
        :return:                json string of movie contents
        """

        movie = (
            Movie.query.join(Director, Director.director_id == Movie.director_id)
            .filter(Director.director_id == director_id)
            .filter(Movie.movie_id == movie_id)
            .one_or_none()
        )

        if movie is not None:
            movie_schema = MovieSchema()
            data = movie_schema.dump(movie)
            return data

        else:
            abort(404, f"Movie not found for Id: {movie_id}")

    def read_one_name(original_title):
        """
        This function responds to a request for /api/movies/{movie_id}
        with one matching movie id from movies

        :param id:   Movie id of movies to find
        :return:            movies matching movie id
        """

        movie = (
            Movie.query.filter(Movie.original_title == original_title)
            .one_or_none()
        )

        if movie is not None:

            movie_schema = MovieSchema()
            data = movie_schema.dump(movie)
            return data

        else:
            abort(404, f"Movie {original_title} not found")

    def read_one_id(movie_id):
        """
        This function responds to a request for /api/movies/{movie_id}
        with one matching movie id from movies

        :param id:   Movie id of movies to find
        :return:            movies matching movie id
        """

        movie = (
            Movie.query.filter(Movie.movie_id == movie_id)
            .one_or_none()
        )

        if movie is not None:

            movie_schema = MovieSchema()
            data = movie_schema.dump(movie)
            return data

        else:
            abort(404, f"Movie with id {movie_id} not found")


    def create(director_id, movie):
        """
        This function creates a new movie related to the passed in director id.

        :param director_id:       Id of the director the movie is related to
        :param movie:            The JSON containing the movie data
        :return:                201 on success
        """

        director = Director.query.filter(Director.director_id == director_id).one_or_none()
        
        movie_uid = movie.get("movie_uid")
        original_title = movie.get("original_title")

        existing_uid = (
            Director.query.filter(Movie.movie_uid == movie_uid)
            .filter(Movie.original_title == original_title)
            .one_or_none()
        )
        
        if director is None:
            abort(404, f"Director not found for Id: {director_id}")
        else:
            
            if existing_uid is None:
                schema = MovieSchema()
                new_movie = schema.load(movie, session=db.session)

                director.movies.append(new_movie)
                db.session.commit()

                data = schema.dump(new_movie)

                return data, 201

            else:
                abort(409, f"Movie with uid of {movie_uid} already exists")


    def update(director_id, movie_id, movie):
        """
        This function updates an existing movie related to the passed in
        director id.

        :param director_id:       Id of the director the movie is related to
        :param movie_id:         Id of the movie to update
        :param content:            The JSON containing the movie data
        :return:                200 on success
        """
        update_movie = (
            Movie.query.filter(Director.director_id == director_id)
            .filter(Movie.movie_id == movie_id)
            .one_or_none()
        )

        movie_uid = movie.get("movie_uid")

        existing_uid = (
            Movie.query.filter(Movie.movie_uid == movie_uid)
            .one_or_none()
        )
        
        if update_movie is not None and existing_uid is not None:

            schema = MovieSchema()
            update = schema.load(movie, session=db.session)

            update.director_id = update_movie.director_id
            update.movie_id = update_movie.movie_id
            update.movie_uid = update_movie.movie_uid

            db.session.merge(update)
            db.session.commit()

            data = schema.dump(update_movie)

            return data, 200

        else:
            abort(404, f"Movie not found for Id: {movie_id} or movie uid cannot be overwritten")


    def delete(director_id, movie_id):
        """
        This function deletes a movie from the movie structure

        :param director_id:   Id of the director the movie is related to
        :param id:     Id of the movie to delete
        :return:            200 on successful delete, 404 if not found
        """

        movie = (
            Movie.query.filter(Director.director_id == director_id)
            .filter(Movie.movie_id == movie_id)
            .one_or_none()
        )

        if movie is not None:
            db.session.delete(movie)
            db.session.commit()
            return make_response(
                "Movie {movie_id} deleted".format(movie_id=movie_id), 200
            )

        else:
            abort(404, f"Movie not found for Id: {movie_id}")
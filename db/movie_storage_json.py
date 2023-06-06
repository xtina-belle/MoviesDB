import json

from MoviesDB.db.movie_storage import MovieDB
from MoviesDB.db.movie_dto import MovieDto

DB_JSON_FILE = "MoviesDB/db/moviesDB.json"


class MovieDBJson(MovieDB):
    def setup(self):
        """Loading the DB data to memory"""
        with open(DB_JSON_FILE, "r", encoding="utf-8") as file:
            for title, movie_data in json.load(file).items():
                self._title_to_movie_dto[title] = MovieDto.get_instance(title, movie_data)

    def _flush_data(self):
        """Flush self._title_to_movie_dto to the json file"""
        with open(DB_JSON_FILE, "w", encoding="utf-8") as file:
            data = {
                title: movie_dto.to_dict()
                for title, movie_dto in self._title_to_movie_dto.items()
            }
            json.dump(data, file, indent=4)
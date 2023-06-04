from MoviesDB.movie_app_client import MovieAppClient


def main():
    """A runner for the app"""
    client = MovieAppClient()
    client.setup()
    client.run()


if __name__ == "__main__":
    main()

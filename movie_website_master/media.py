import webbrowser

class Movie():
    """ This class provides a way to store movie related information

    Args:
        movie_title (str): The title of the movie
        launch_year (str): The year the movie was launched
        movie_rating (str): The movie´s IMDB Website rating
        poster_image (str): A url pointing to the poster of the movie
        trailer_youtube(str): A url pointing to the trailer of the movie on youtube

    Attributes:
        movie_title (str): The title of the movie
        launch_year (str): The year the movie was launched
        movie_rating (str): The movie´s IMDB Website rating
        poster_image (str): A url pointing to the poster of the movie
        trailer_youtube(str): A url pointing to the trailer of the movie on youtube
    """


    def __init__(self, movie_title, launch_year, movie_rating, poster_image, trailer_youtube):
        self.title = movie_title
        self.year = launch_year
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube



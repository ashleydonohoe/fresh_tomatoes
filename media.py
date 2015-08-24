import webbrowser

# class to store movie information

class Movie():

    """
    Class used to store the movie title, storyline, release year, poster image
    and YouTube trailer.
    """

    def __init__(self, movie_title, movie_storyline, movie_year,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.year = movie_year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

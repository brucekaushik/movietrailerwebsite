import webbrowser

class Movie():
    '''
    This class provides a way to store movie related information and play its youtube trailer

    movie_title (str): title of the movie
    movie_storyline (str): storyline of the movie, used if unable to fetch one from the OMDB API
    movie_poster_image_url (str): poster image url of the movie
    movie_youtube_trailer_url (str): youtube trailer url of the movie
    '''

    def __init__(self, movie_title, movie_storyline, movie_poster_image_url, movie_youtube_trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.youtube_trailer_url = movie_youtube_trailer_url


    def show_trailer(self):
        ''' open web browser and play the youtube trailer '''

        webbrowser.open(self.youtube_trailer_url)

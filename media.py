import webbrowser
import urllib
import json

class Movie():
    '''
    This class provides a way to store movie related information and play its youtube trailer
    Storyline of the movie is fetched from the OMDB's REST API

    movie_title (str): title of the movie
    movie_storyline (str): storyline of the movie, used if unable to fetch one from the OMDB API
    movie_poster_image_url (str): poster image url of the movie
    movie_youtube_trailer_url (str): youtube trailer url of the movie
    '''

    def __init__(self, movie_title, movie_storyline, movie_poster_image_url, movie_youtube_trailer_url):
        '''
        initialize the required instance variables

        movie_title (str): title of the movie
        movie_storyline (str): storyline of the movie, used if unable to fetch one from the OMDB API
        movie_poster_image_url (str): poster image url of the movie
        movie_youtube_trailer_url (str): youtube trailer url of the movie
        '''

        self.title = movie_title
        self.storyline = self.get_storyline(movie_title, movie_storyline)
        self.poster_image_url = movie_poster_image_url
        self.youtube_trailer_url = movie_youtube_trailer_url

    def get_storyline(self, movie_title, movie_storyline):
        '''
        get the storyline from OMDB's REST API
        if the storyline could not be fetched, use the passed storyline

        movie_title (str): title of the movie
        movie_storyline (str): storyline of the movie
        '''

        # format movie title to query api
        movie_title = movie_title.replace(' ', '+')

        # query the api and observe the store the response in a variable
        response = urllib.urlopen('http://www.omdbapi.com/?t=' + movie_title + '&y=&plot=short&r=json')
        data = response.read()

        # check for proper response, and determine which storyline to use (passed/fetched)
        if(data):
            data = json.loads(data)
            try:
                storyline = data['Plot'] + '<br/><br/>(fetched from API)'
            except KeyError:
                storyline = movie_storyline + '<br/><br/>(could not fetch storyline from API)'

            return storyline
        else:
            return movie_storyline + ' (could not fetch storyline from API)'


    def show_trailer(self):
        ''' open web browser and play the youtube trailer '''

        webbrowser.open(self.youtube_trailer_url)

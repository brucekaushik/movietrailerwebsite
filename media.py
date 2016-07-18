import webbrowser
import requests

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

        movie_title = movie_title.replace(' ', '+')

        response = requests.get('http://www.omdbapi.com/?t=' + movie_title + '&y=&plot=short&r=json')

        if(response.status_code == 200):
            data = response.json()
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

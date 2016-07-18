import media
import fresh_tomatoes

# create the required movie objects
yevade_subramanyam = media.Movie("Yevade Subramanyam",
                      "A guy finds himself after a journey to Doodh Kashi",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/e/e6/Yevade_Subramanyam_first_poster.jpg/220px-Yevade_Subramanyam_first_poster.jpg",
                      "https://www.youtube.com/watch?v=_pqngUO_pP4")

bahubali = media.Movie("Bahubali (2016)",
                      "In ancient India, an adventurous and daring man becomes involved in a decades old feud between two warring people.",
                      "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
                      "https://www.youtube.com/watch?v=sOEg_YZQsTI")

sultan = media.Movie("Sultan (2016)",
                     "A middle-aged wrestling champion (Salman Khan) tries to make a comeback to represent India at the Olympics.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/3/31/Sultan%27s_logo.jpg/220px-Sultan%27s_logo.jpg",
                      "https://www.youtube.com/watch?v=wPxqcq6Byq0")

manam = media.Movie("Manam",
                     "Bittu, a six-year-old, loses his parents in an unfortunate car accident",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Manam_poster.jpg/220px-Manam_poster.jpg",
                      "https://www.youtube.com/watch?v=Y4Bq4SQc_eM")

oopiri = media.Movie("Oopiri",
                     "After he becomes a quadriplegic from an accident, Vikram hires a young man to be his caregiver.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/4/49/Oopiri_Telugu_film_Poster.jpg/220px-Oopiri_Telugu_film_Poster.jpg",
                      "https://www.youtube.com/watch?v=e1ddsJ38D5Q")

kumari_21f = media.Movie("Kumari 21F",
                     "A young man's love for his girlfriend is tested by the rumors surrounding her.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/Kumari_21F_poster.jpg/220px-Kumari_21F_poster.jpg",
                      "https://www.youtube.com/watch?v=Twk9hBSdVsM")


# store the movie objects in a list to create a template
movies = [yevade_subramanyam, bahubali, sultan, manam, oopiri, kumari_21f]

# create movies template & open in browser
fresh_tomatoes.open_movies_page(movies)




import media
import fresh_tomatoes

# add movie details
toy_story = media.Movie("Toy Story",
                        "Kids and toys adventure together",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "Man on a mission",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg"  # NOQA,
                     "www.youtube.com/watch?v=8KAtG68bIUc")
boondock_saints = media.Movie("Boondock Saints",
                              "Vigilante brothers",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/The_Boondock_Saints_poster.jpeg/215px-The_Boondock_Saints_poster.jpeg",  # NOQA
                              "https://www.youtube.com/watch?v=ydXojYfCF3I")
rear_window = media.Movie("Rear Window",
                          "Catching murderers",
                          "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Rear_Window_film_poster.jpg/225px-Rear_Window_film_poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=6kCcZCMYw38")
donnie_darko = media.Movie("Donnie Darko",
                           "What it means to be alive",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Donnie_Darko_poster.jpg/220px-Donnie_Darko_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=ZZyBaFYFySk")
sixth_sense = media.Movie("The Sixth Sense",
                          "Dark secrets",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/6/66/The_sixth_sense.jpg/220px-The_sixth_sense.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=VG9AGf66tXM")

# create movies collection
movies = [toy_story, avatar, boondock_saints, rear_window, donnie_darko,
          sixth_sense]

# updates movies page
fresh_tomatoes.open_movies_page(movies)

print (media.Movie.__doc__)

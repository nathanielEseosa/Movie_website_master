"""This module provides a way to store movie related information."""
import media

"""This module has a function that takes in one argument, which is a list of movies and creates an HTML file which visualizes all of your favorite movies."""
import fresh_tomatoes

the_road = media.Movie("The Road",
                        "2009", "7,3/10",
                        "https://jeroenthoughts.files.wordpress.com/2015/06/the-road3.jpg",
                        "https://www.youtube.com/watch?v=94KcI0gLq1A&t=49s")


the_good_the_bad_and_the_ugly = media.Movie("The Good, the Bad and the Ugly",
                                            "1966", "8,9/10",
                                            "https://images-na.ssl-images-amazon.com/images/M/MV5BOTQ5NDI3MTI4MF5BMl5BanBnXkFtZTgwNDQ4ODE5MDE@._V1_SY1000_CR0,0,656,1000_AL_.jpg",
                                            "https://www.youtube.com/watch?v=wrLEVv-Lh7U")


the_assassination_of_jesse_james = media.Movie("The Assassination of Jesse James by the Coward Robert Ford",
                                               "2007", "7,5/10",
                                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY2NDI2MTc2NV5BMl5BanBnXkFtZTcwNjA2NTQzMw@@._V1_UY1200_CR91,0,630,1200_AL_.jpg",
                                    "https://www.youtube.com/watch?v=SrGmmitc62Q")

apocalypto = media.Movie("Apocalypto",
                        "2006", "7,8/10",
                         "https://s-media-cache-ak0.pinimg.com/originals/eb/18/c1/eb18c155cd544f1100a3e699ae4ed7c8.jpg",
                         "https://www.youtube.com/watch?v=gSw5l5jMnPM")

the_godfather = media.Movie("The Godfather",
                            "1972", "9,2",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BY2Q2NzQ3ZDUtNWU5OC00Yjc0LThlYmEtNWM3NTFmM2JiY2VhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,700,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")

legends_of_the_fall = media.Movie("Legends of the Fall",
                                    "1994", "7,5/10",
                                  "https://static.rogerebert.com/uploads/movie/movie_poster/legends-of-the-fall-1995/large_uh0sJcx3SLtclJSuKAXl6Tt6AV0.jpg",
                                  "https://www.youtube.com/watch?v=jyR5NFhivdM")

movies = [the_road, the_good_the_bad_and_the_ugly, the_assassination_of_jesse_james, apocalypto, the_godfather, legends_of_the_fall]
fresh_tomatoes.open_movies_page(movies)

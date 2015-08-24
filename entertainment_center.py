import media
import fresh_tomatoes

#Created objects for each of the six movies along with data for each movie 

eurotrip = media.Movie("Eurotrip", "High school friends go to Europe", "2004", "http://www.gstatic.com/tv/thumb/movieposters/33823/p33823_p_v7_ac.jpg", "https://www.youtube.com/watch?v=SeoX8MZd81E")

matilda = media.Movie("Matilda", "A little girl has a special gift", "1996", "http://static.rogerebert.com/uploads/movie/movie_poster/matilda-1996/large_zvgm8Yckvd12iZFaXRXbblcRcO8.jpg", "https://www.youtube.com/watch?v=pnzLRDDijW0")

ferris = media.Movie("Ferris Bueller's Day Off", "A high school student takes a day off", "1986", "http://www.gstatic.com/tv/thumb/movieposters/9316/p9316_p_v7_aa.jpg", "https://www.youtube.com/watch?v=R-P6p86px6U")

billy_madison = media.Movie("Billy Madison", "A grown man returns to school", "1995", "http://www.gstatic.com/tv/thumb/movieposters/16468/p16468_p_v7_af.jpg", "https://www.youtube.com/watch?v=_-PZeKhMdiQ")

arranged = media.Movie("Arranged", "Two very different teachers become friends", "2007", "http://www.gstatic.com/tv/thumb/dvdboxart/175811/p175811_d_v7_aa.jpg", "https://www.youtube.com/watch?v=fP9tnjaXrDk")

christmas_vacation = media.Movie("National Lampoon's Christmas Vacation", "A perfect Christmas goes wrong", "1989", "https://upload.wikimedia.org/wikipedia/en/5/53/NationalLampoonsChristmasVacationPoster.JPG", "https://www.youtube.com/watch?v=decUIVkZ4GI")

movies = [eurotrip, matilda, ferris, billy_madison, arranged, christmas_vacation]

#opens the page showing the movie trailers
fresh_tomatoes.open_movies_page(movies)
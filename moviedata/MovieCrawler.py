"""This program is meant to crawl through my files and get information for all the movies I have"""
from imdb import IMDb
from datetime import datetime
import os
import MovieParser


path = raw_input("Enter filepath: ")

ia = IMDb('http')

previous_title = ""
for file in os.listdir(path):
    index = 0 #the index of the movie in the list of movies
    fileTitle = ""
    fileTitle = file[0:file.index(".")] #title of file in directory without .mp4, .avi, or .mkv

    try:
        list_of_results = ia.search_movie(fileTitle) #the list of movies based on the file title given
        movie = list_of_results[index] #gets the movie at the current index
        ia.update(movie) #gets all information based on the movie selected

        query_title = MovieParser.parse_title(movie) #the title of the movie
        query_year = MovieParser.parse_year(movie) #the year the movie was made

        #ensures that movies are not repeated because of title similarities
        if previous_title == query_title or (query_year < 1989 or query_year > datetime.year):
            index += 1
            movie = list_of_results[index]
            ia.update(movie)  # gets all information based on the movie selected
            query_title = MovieParser.parse_title(movie)
            query_year = MovieParser.parse_year(movie)

        query_director = MovieParser.parse_director(movie) #gets director of movie
        query_cast = MovieParser.parse_cast(movie) #gets cast of movie
        query_producer = MovieParser.parse_producer(movie) #gets producer of movie
        query_writer = MovieParser.parse_writer(movie) #gets writer of movie
        query_rating = MovieParser.parse_MPAA(movie) #gts MPAA rating for movie

        previous_title = query_title #gets the previous title for future use
    except IndexError:
        print "error"

    #removes the (I) and (II) that are sometimes in front of movies
    if query_title.endswith(" (I)"):
        query_title = query_title.replace(" (I)", "")
    elif query_title.endswith(" (II)"):
        query_title = query_title.replace(" (II)", "")

    # TODO: Figure out a way to write to file so that you don't have to rewrite everything over
    f = open(path + "/moviedata.txt", 'a')
    movie_info = query_title + "\n" + str(query_year) + "\n" + query_director + "\n" + query_producer + "\n" + \
                 query_writer + "\n" + query_cast + "\n" + str(query_rating) + "\n"
    f.write(movie_info.encode("utf-8"))
    f.write("*************************************************\n")
    f.close()

print "Done getting information"








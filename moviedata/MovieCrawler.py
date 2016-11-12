"""This program is meant to crawl through my files and change the meta data for all the movies I have"""
from imdb import IMDb
import os

path = "C:\Mihir\Popcorn Time\Movies"

ia = IMDb('http')

for file in os.listdir(path):
    fileTitle = ""
    if (file.endswith(".mp4")):
        fileTitle = file.replace(".mp4", "")
    elif (file.endswith(".avi")):
        fileTitle = fileTitle.replace(".avi", "")
    elif (file.endswith(".mkv")):
        fileTitle = fileTitle.replace(".mkv", "")

    try:
        query_string = ia.search_movie(fileTitle)[0]
    except IndexError:
        print ia.search_movie(fileTitle)

    print query_string






"""This program is meant to crawl through my files and change the meta data for all the movies I have"""
import os

path = raw_input("Please put full path to directory with movie files\n")

os.chdir(path)

for file in os.listdir(path):
    name = file.title()
    name = name[0:name.index(".")]

    print name

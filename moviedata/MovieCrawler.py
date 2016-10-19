"""This program is meant to crawl through my files and change the meta data for all the movies I have"""
import os

path = raw_input("Please put full path to directory with movie files\n")

os.chdir(path)

num_mp4 = 0
num_mkv = 0
num_avi = 0

for file in os.listdir(path):
    if file.endswith(".mp4"):
        num_mp4 += 1
    elif file.endswith(".mkv"):
        num_mkv += 1
    elif file.endswith(".avi"):
        num_avi += 1

print "Number of .mp4: " + str(num_mp4)
print "Number of .mkv: " + str(num_mkv)
print "Number of .avi: " + str(num_avi)
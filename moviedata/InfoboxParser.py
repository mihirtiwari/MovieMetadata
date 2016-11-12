"""Does all the parsing from the Wikipedia infobox"""

import requests
from bs4 import BeautifulSoup

def get_infobox_type(type, name):
    if (type == "Movies"):
        movie_infobox(name)


    """Gets data for an infobox if the page is for a movie. Data contains details such as director, producer(s), etc"""
def movie_infobox(name):
    wiki_end = wikipedia_valid(name)

    request = requests.get("https://en.wikipedia.org/wiki/" + wiki_end)

    soup = BeautifulSoup(request.text, "html.parser")

    infobox = soup.find("table", class_="infobox")
    director = infobox.find("th", text="Directed by").next_sibling.next_sibling
    producer = infobox.find("th", text="Produced by").next_sibling.next_sibling
    screenplay = infobox.find("th", text="Screenplay by").next_sibling.next_sibling
    stars = infobox.find("th", text="Starring").next_sibling.next_sibling
    music = infobox.find("th", text="Music by").next_sibling.next_sibling



    """Makes the name such that it is "Wikipedia" searchable e.g. underscores where there are spaces, etc"""
def wikipedia_valid(name):
    return name


movie_infobox("127_Hours")
"""Gets the director(s) of the movie separated by commas"""
def parse_director(movie):
    director = "NA"
    if movie.has_key('director'):
        director = ""
        for name in movie.get('director'):
            director += name.get('name') + ", "

    return director

"""Gets max 15 members of the movie cast separated by commas"""
def parse_cast(movie):
    cast = "NA"
    index = 1
    if (movie.has_key('cast')):
        cast = ""
        for member in movie.get('cast'):
            cast += member.get('name') + ", "
            index += 1

            if index > 15:
                return cast

    return cast

"""Gets max 3 producer(s) separated by commas"""
def parse_producer(movie):
    producer = "NA"
    index = 1
    if (movie.has_key('producer')):
        producer = ""
        for prod in movie.get('producer'):
            producer += prod.get('name') + ", "
            index += 1

            if index > 3:
                return producer

    return producer

"""Gets max 3 writer(s) separated by commas"""
def parse_writer(movie):
    writer = "NA"
    index = 1
    if movie.has_key('writer'):
        writer = ""
        for prod in movie.get('writer'):
            writer += prod.get('name') + ", "
            index += 1

            if index > 3:
                return writer

    return writer

"""Gets the title of the movie"""
def parse_title(movie):
    if movie.has_key('title'):
        title = str(movie['title'])
        return title

    return "NA"

"""Gets the year movie was made"""
def parse_year(movie):
    if movie.has_key('year'):
        year = movie['year']
        return year

    return "NA"

"""Gets the MPAA rating"""
def parse_MPAA(movie):
    if (movie.has_key('mpaa')):
        temp_rating = movie['mpaa']
        rating = temp_rating.split(" ")[1]
        return rating

    return "NA"
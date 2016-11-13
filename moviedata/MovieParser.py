"""Gets the director(s) of the movie separated by commas"""
def parse_director(movie):
    director = ""
    for name in movie.get('director'):
        director += name.get('name') + ", "

    return director

"""Gets max 15 members of the movie cast separated by commas"""
def parse_cast(movie):
    cast = ""
    index = 1
    for member in movie.get('cast'):
        cast += member.get('name') + ", "
        index += 1

        if index > 15:
            break


    return cast

"""Gets max 3 producer(s) separated by commas"""
def parse_producer(movie):
    producer = ""
    index = 1
    for prod in movie.get('producer'):
        producer += prod.get('name') + ", "
        index += 1

        if index > 3:
            break

    return producer

"""Gets max 3 writer(s) separated by commas"""
def parse_writer(movie):
    writer = ""
    index = 1
    for prod in movie.get('producer'):
        writer += prod.get('name') + ", "
        index += 1

        if index > 3:
            break

    return writer

"""Gets the title of the movie"""
def parse_title(movie):
    title = str(movie['title'])

    return title

"""Gets the year movie was made"""
def parse_year(movie):
    year = movie['year']
    return year
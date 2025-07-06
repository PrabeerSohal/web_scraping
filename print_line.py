with open("movies.html") as f:
    for i in f:
        if 'Metascore' in i:
            print(i)


def readFile(filename):
    filenames = filename.split()
    with open(filenames[0], "rt") as fp:
        datas = fp.read()
        data = datas.split("\n")

    genres = []
    for d in data:
        movie = d.split("::")
        genres.append(movie)

    genre = []
    for g in genres:
        genre.append(g[2])
    #print(genre)

    gen = []
    for g in genre:
        gen.append(g.split("|"))
    #print(gen)

    genre.clear()
    genre = ["Animation", "Children's", "Comedy", "Adventure", "Fantasy", "Romance", "Drama", "Action", "Crime", "Thriller", "Horror", "Sci-Fi", "Documentary"]
    cnt = [0 for i in range(len(genre))]
    #print(cnt)

    idx1 = 0
    idx2 = 0
    while idx1 != len(genre):
        for g in gen:
            for i in g:
                if i == genre[idx1]:
                    cnt[idx2] += 1
        idx1 += 1
        idx2 += 1
    #print(cnt)
    #i = 0
    #for g in genre:
        #print(g, cnt[i])
        #i += 1
    with open(filenames[1], "wt") as fp:
        i = 0
        for g in genre:
            fp.write(g + " " +  str(cnt[i]) + "\n")
            i += 1


filename = input()
readFile(filename)

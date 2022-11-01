#!/usr/bin/python3
import sys

params = list(sys.argv)
#print(params)
inputFile = params[1]
outputFile = params[2]
#print(inputFile, outputFile)

def genreCount(inputFile, outputFile):
    with open(inputFile, "rt") as fp:
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
    cnt = [0 for i in range(18)]
    
    for g in gen:
        for i in g:
            if i not in genre:
                genre.append(i)
    #print(genre)
    
    genIdx = 0
    cntIdx = 0
    while cntIdx != len(genre):
        for g in gen:
            for i in g:
                if i == genre[genIdx]:
                    cnt[cntIdx] += 1
        genIdx += 1
        cntIdx += 1
    #print(genre, cnt)
    
    with open(outputFile, "wt") as fp:
        i = 0
        for g in genre:
            fp.write(g + " " +  str(cnt[i]) + "\n")
            i += 1

genreCount(inputFile, outputFile)

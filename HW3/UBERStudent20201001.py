#!/usr/bin/python3
import sys
import calendar

inputFile = sys.argv[1]
outputFile = sys.argv[2]

data = []
with open(inputFile, "rt") as fp:
    datas = fp.read()
    data.append(datas.split("\n"))
    #print(data)
    
    information = []
    for dat in data:
        #print(dat)        
        for d in dat:
            #print(d)
            dInfo = d.split(",")
            information.append(dInfo)
    #print(information)

    region = []
    for info in information:
        #print(info[0])
        if info[0] not in region:
            region.append(info[0])
    #print(region)
    
    dayOfWeek = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    vehicles = [[0 for i in range(len(dayOfWeek))] for i in range(len(region))]
    trips = [[0 for i in range(len(dayOfWeek))] for i in range(len(region))]
    #print(vehicles)
    #print(trips)
    
    for info in information:
        #print(info[1])
        date = info[1].split("/")
        mon = int(date[0])
        day = int(date[1])
        year = int(date[2])

        dayNum = calendar.weekday(year, mon, day) 
        #print(mon, day, year, dayNum, dayOfWeek[dayNum])
        #print(vehicles)
        idx = 0
        for r in region:
            if r == info[0]:
                vehicles[idx][dayNum] += int(info[2])
                trips[idx][dayNum] += int(info[3])
            #print(r, vehicles[idx][dayNum], trips[idx][dayNum])
            idx += 1
    #print(vehicles)
    #print(trips)
      
with open(outputFile, "wt") as fp:
    j = 3
    for d in dayOfWeek: 
        i = 0
        for r in region:
            fp.write("{},{} {},{}\n".format(r, dayOfWeek[j], vehicles[i][j], trips[i][j]))
            i += 1
        j += 1
        if j == 7:
            j = 0


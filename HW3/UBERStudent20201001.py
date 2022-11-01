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

    dic = dict()
    #region = []
    for info in information:
        #print(info[0])
        #if info[0] not in region:
            #region.append(info[0])
        if info[0] not in dic:
            dic[info[0]] = {}
    #print(region)
    
    dayOfWeek = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    #vehicles = [[0 for i in range(len(dayOfWeek))] for i in range(len(region))]
    #trips = [[0 for i in range(len(dayOfWeek))] for i in range(len(region))]
    #print(vehicles)
    #print(trips)
    
    for info in information:
        #print(info[1])
        date = info[1].split("/")
        mon = int(date[0])
        day = int(date[1])
        year = int(date[2])

        dayNum = calendar.weekday(year, mon, day) 
        info[1] = dayOfWeek[dayNum]

        if info[1] not in dic[info[0]]:
            dic[info[0]][info[1]] = {}
            dic[info[0]][info[1]]['vehicles'] = int(info[2])
            dic[info[0]][info[1]]['trips'] = int(info[3])
        else:   
            dic[info[0]][info[1]]['vehicles'] += int(info[2])
            dic[info[0]][info[1]]['trips'] += int(info[3])
        #print(mon, day, year, dayNum, dayOfWeek[dayNum])
        #print(vehicles)
        idx = 0
#print(dic)

with open(outputFile, "wt") as fp:
    for region in dic:
        for weekDay in dic[region]:
            fp.write("{},{} {},{}\n".format(region, weekDay, dic[region][weekDay]['vehicles'], dic[region][weekDay]['trips']))

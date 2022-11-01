#!/usr/bin/python3
import sys
import calendar

inputFile = sys.argv[1]
outputFile = sys.argv[2]

dic = dict()
with open(inputFile, "rt") as fp:
    for line in fp:
        line = line.replace("\n", "")
        info = line.split(",")
        #print(info)
        
        if info[0] not in dic:
            dic[info[0]] = {}
        #print(info[0])

        dayOfWeek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        
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
#print(dic)

with open(outputFile, "wt") as fp:
    for region in dic:
        for weekDay in dic[region]:
            fp.write("{},{} {},{}\n".format(region, weekDay, dic[region][weekDay]['vehicles'], dic[region][weekDay]['trips']))

#!/usr/bin/python3
import sys
import calendar
inputFile = sys.argv[1]
outputFile = sys.argv[2]

uber_dict = {}
with open(inputFile,"rt") as f:
    with open(outputFile,"wt") as output:
        for line in f:
            uber_array=line.strip().split(',')
            # print(uber_array)
            region=uber_array[0]
            # print(uber_array[1])
            date_array = uber_array[1].split('/')
            # print(date_array,date_array[0])
            year=int(date_array[2])
            month=int(date_array[0])
            day = int(date_array[1])
            wday = calendar.weekday(year,month,day)
            # print(wday)
            dayofweek  = ['MON','TUE','WED','THU','FRI','SAT','SUN']
            day_name = dayofweek[wday]
            vehicles = uber_array[2]
            trips=uber_array[3]
            # print(day_name)
        

        
            output.write("%s,%s %d,%d\n" % (region, day_name, int(vehicles), int(trips)))

#!/usr/bin/python3
import sys
import calendar
inputFile = sys.argv[1]
outputFile = sys.argv[2]

uber_dict = []
with open(inputFile,"rt") as f:
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
            vehicles = int(uber_array[2])
            trips=int(uber_array[3])
            # print(day_name)

            u_dict = {
                "region":region,
                "day_name":day_name,
                "vehicles":vehicles,
                "trips":trips,
            }
            uber_dict.append(u_dict)    

sort_uber = sorted(uber_dict,key=lambda x: x['region'])

with open(outputFile,"wt") as output:
        for u_dict in sort_uber:
            output.write("%s,%s %d,%d\n" % (u_dict["region"], u_dict["day_name"], u_dict["vehicles"], u_dict["trips"]))
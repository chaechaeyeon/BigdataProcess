#!/usr/bin/python3
import sys
def parse_date(date_str):
    # Parse date in the format "month/day/year" and return the day of the week
    month, day, year = map(int, date_str.split('/'))
    import datetime
    day_of_week = datetime.date(year, month, day).strftime("%a").upper()
    return day_of_week
if len(sys.argv) != 3:
    print("Usage: python3 UBERStudent<Your ID>.py input_file output_file")
    sys.exit(1)

inputFile = sys.argv[1]
outputFile = sys.argv[2]

# Dictionary to store vehicle and trip data
data = {}

with open(inputFile, "r") as file:
    for line in file:
        parts = line.strip().split(',')
        if len(parts) == 4:
            region, date, vehicles, trips = parts
            day = parse_date(date)
            if region not in data:
                data[region] = {}
            if day not in data[region]:
                data[region][day] = [0, 0]
            data[region][day][0] += int(vehicles)
            data[region][day][1] += int(trips)

with open(outputFile, "w") as output:
    for region, days in data.items():
        for day, values in days.items():
            vehicles, trips = values
            output.write(f"{region},{day} {vehicles},{trips}\n")



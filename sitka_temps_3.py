import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

'''
print(header_row)

for index, column_header in enumerate(header_row): #gives position and value of index
    print(index,column_header)
'''
highs = []
lows = []
dates = [] #want to give dates

'''
x = datetime.strptime("2018-07-01", "%Y-%m-%d")
print(x)
'''

for row in csv_file:
    lows.append(int(row[6])) #index of tempmin
    highs.append(int(row[5]))
    the_date = datetime.strptime(row[2], "%Y-%m-%d") #index of date, formats the date
    dates.append(the_date)


import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, lows, c="blue", alpha = 0.5)
plt.plot(dates, highs, c="red", alpha = 0.5)

plt.title("Daily High/Low Temps, 2018", fontsize = 16)
plt.xlabel("", fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis="both",labelsize = 16) 

plt.fill_between(dates, highs, lows, facecolor = "blue", alpha = 0.1) #needs to know the x and the y1,y2 to fill between the gap

fig.autofmt_xdate() #formats the xaxis with the fig created 

plt.show()
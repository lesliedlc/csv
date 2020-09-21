import csv

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

'''
print(header_row)

for index, column_header in enumerate(header_row): #gives position and value of index
    print(index,column_header)
'''

highs = []

for row in csv_file:
    highs.append(int(row[5])) 

print(highs)

import matplotlib.pyplot as plt

plt.plot(highs, c="red")

plt.title("Daily High Temps, July 2018", fontsize = 16)
plt.xlabel("")
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis="both",which="major",labelsize = 16) #only want major ticks to show on both axis

plt.show()
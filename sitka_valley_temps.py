import csv
from datetime import datetime

open_sitka = open("sitka_weather_2018_simple.csv", "r")
open_valley = open("death_valley_2018_simple.csv", "r")

csv_valley = csv.DictReader(open_valley, delimiter=",")
csv_sitka = csv.DictReader(open_sitka, delimiter=",")

header_sitka = next(csv_sitka)
header_valley = next(csv_valley)

high_s, low_s, date_s = [],[],[]
high_v, low_v, date_v = [],[],[]

#information for sitka 
for row in csv_sitka:
    try:
        high = int(row["TMAX"])
        low = int(row["TMIN"])
        current_date = datetime.strptime(row["DATE"], "%Y-%m-%d") #index of date, formats the date
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        low_s.append(int(row["TMIN"])) #index of tempmin 6
        high_s.append(int(row["TMAX"])) #5
        date_s.append(current_date)

#information for death valley 
for row in csv_valley:
    try:
        highdv = int(row["TMAX"])
        lowdv = int(row["TMIN"])
        current_date = datetime.strptime(row["DATE"], "%Y-%m-%d") #index of date, formats the date
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        low_v.append(int(row["TMIN"])) #index of tempmin
        high_v.append(int(row["TMAX"]))
        date_v.append(current_date)

import matplotlib.pyplot as plt

fig,ax = plt.subplots(2)

#sitka date/temp
ax[0].plot(date_s, low_s, c="blue", alpha = 0.5)
ax[0].plot(date_s, high_s, c="red", alpha = 0.5)
#valley date/temp
ax[1].plot(date_v, low_v, c="blue", alpha = 0.5)
ax[1].plot(date_v, high_v, c="red", alpha = 0.5)

#sitka graph
ax[0].set_title(header_sitka["NAME"], fontsize = 12)
ax[0].tick_params(axis="both",labelsize = 12) 
ax[0].fill_between(date_s, high_s, low_s, facecolor = "blue", alpha = 0.1)
#deathvalley graph
ax[1].set_title(header_valley["NAME"], fontsize = 12)
ax[1].tick_params(axis="both",labelsize = 12) 
ax[1].fill_between(date_v, high_v, low_v, facecolor = "blue", alpha = 0.1)

fig.autofmt_xdate() #formats the xaxis with the fig created 

fig.suptitle("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US", fontsize = 11)
plt.show()


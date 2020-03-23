'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)
    I think that the increase in traffic over the past 10 years is responsible for the increase in rail usage.
    I believe that the amount of total riders decreased incrementally because of the introduction of bikes and ride share technology like divvy, uber, and lyft


'''

import csv
import matplotlib.pyplot as plt


with open('cta_dataset.csv') as f:
    reader = csv.reader(f)  # makes a reader object
    data = list(reader)

headers = data.pop(0)
print(headers)

last_10_years = [int(x[0]) for x in data[-10:]]

rail_10 = [int(x[3]) for x in data[-10:]]

bus_10 = [int(x[1]) for x in data[-10:]]

total_10 = [int(x[4]) for x in data[-10:]]


plt.figure(1)
plt.plot(last_10_years, rail_10, label='Rails')
plt.plot(last_10_years, bus_10, label='Bus')
plt.plot(last_10_years, total_10, label='Total')

plt.title("2009 - 2018 CTA Rider Data", fontsize=18, color='black')
plt.xlabel('Year')
plt.ylabel('Riders')
plt.legend()

plt.show()
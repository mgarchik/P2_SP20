
'''
Greenhouse gas emissions (GHG) vs. square footage for all school buildings in Chicago
Data set used will be Chicago Energy Benchmark info from 2018
data can be found at...
https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD
Energy Efficiency of Chicago Schools (35pts)
Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The dataset at the link above is that data from 2015 to 2018.
We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
Challenge (for fun):
An efficient school would have a large ratio of sqft to ghg.
It would also be interesting to know where Parker lies on this graph???  Let's find out.
Make a scatterplot which does the following:
- Scatter plot the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (10pts)
- Data includes ONLY data for K-12 Schools. (5pts)
- Data includes ONLY data for 2018 reporting. (5pts)
- Label x and y axis and give appropriate title. (5pts)
- Annotate Francis W. Parker. (5pts)
- Create a best fit line for schools shown. (5pts)
Extra Credit: Add a significant feature to your graph that helps tell the story of your data.  (feel free to use methods from matplotlib.org). (10pts)
Note: With extra credit you will earn you a max of 35pts (100%) for the assignment.
Maybe you can try one of the following or think up your own:
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities.
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)
Note 2:  This is a tough assignment to do on your own.  Do your best with what you have.  We will do
'''


import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors
import matplotlib.cm

with open("Chicago_Energy_Benchmarking.csv") as f:
    reader = csv.reader(f)
    raw_data = list(reader)

header = raw_data.pop(0)
print(header)

ghg_index = header.index("Total GHG Emissions (Metric Tons CO2e)")
sqft_index = header.index("Gross Floor Area - Buildings (sq ft)")
type_index = header.index("Primary Property Type")
name_index = header.index("Property Name")
year_index = header.index("Data Year")


valid_data = []

for building in raw_data:
    try:
        float(building[ghg_index])
        float(building[sqft_index])
        if building[type_index] == "K-12 School" and building[0] == "2018":
            valid_data.append(building)
    except:
        pass

ghg = [float(x[ghg_index]) for x in valid_data]
sqft = [float(x[sqft_index]) for x in valid_data]
names = [x[name_index] for x in valid_data]

p = np.polyfit(sqft, ghg, 1)
x = [x for x in range(700000)]
y = [(p[0] * y + p[1]) for y in x]

print(p)

# ratios = [(sqft[x] * p[0]) / (ghg[x] * -p[1]) for x in range(len(names))]
ratios = [sqft[x] / ghg[x] for x in range(len(names))]
mx = max(ratios)
mn = min(ratios)
print(mx)
print(mn)


plt.figure("School Emissions", figsize=(10, 6))
plt.grid(color="gray")

plt.scatter(sqft, ghg, cmap='RdYlGn', c=ratios, norm=matplotlib.colors.Normalize(vmax=mx-170, vmin=mn, clip=True), alpha=.7)
plt.scatter(sqft[names.index("Francis W Parker School")], ghg[names.index("Francis W Parker School")],
            c='blue', label='Francis W. Parker')
plt.scatter([0], [6000], c='white', label="Other Schools")

plt.ylabel("Total GHG Emissions (Metric Tons CO2e)")
plt.xlabel("Gross Floor Area - Buildings (sq ft)")
plt.title("Emissions vs Area")

plt.annotate(names[names.index("Francis W Parker School")], xy=(sqft[names.index("Francis W Parker School")], ghg[names.index("Francis W Parker School")]))

p = np.polyfit(sqft, ghg, 1)
x = [x for x in range(700000)]
y =[(p[0] * y + p[1]) for y in x]
plt.plot(x, y)

plt.legend()

plt.show()
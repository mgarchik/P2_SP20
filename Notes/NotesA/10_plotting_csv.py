import csv
import matplotlib.pyplot as plt

with open("Libraries_-_2019_Visitors_by_Location.csv") as f:
    reader = csv.reader(f)  # makes a reader object
    data = list(reader)

# plot the attendance for our favorite library
header = data.pop(0)
print(header)

library_names = [x[0] for x in data]
print(library_names)

sulzer_index = library_names.index("Sulzer Regional Library")
print(sulzer_index)

sulzer_data = data[sulzer_index]
print(sulzer_data)

sulzer_by_month = sulzer_data[3:-1]
print(sulzer_by_month)

sulzer_by_month = [int(x) for x in sulzer_by_month]
print(sulzer_by_month)
'''
Sorting and Intro to Big Data Problems (22pts)

Import the data from NBAStats.py.  The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
'''
from NBAStats import data
data2 = [x for x in data]
print(data)
print(data2)
data2.pop(0)

#1  Pop off the first item in the list and print it.  It contains the column headers. (1pt)
headings = data.pop(0)
print(headings)

#2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)
data.sort(key=lambda x: x[-1], reverse=True)
for i in range(10):
    print(data[i][2])

#3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)
kobe_pts = 0
for i in range(len(data)):
    if data[i][2] == "Kobe Bryant":
        kobe_pts += int(data[i][-1])
print(kobe_pts)
#4  What player has the most 3point field goals in a single season. (3pts)
data.sort(key=lambda x: x[34], reverse=True)
print(data)
print(data[0][2], "made", data[0][34], "three pointers in one season")

#5  One stat featured in this data set is Win Shares(WS).
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data.  It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time? (4pts)
print(headings)
data2.sort(key=lambda x: x[25], reverse=True)
print(data2[0])
print(data2[0][2], "had the highest one season ws/48 with a", data2[0][25], "ws/48")

#6  Write your own question that you have about the data and provide an answer (4pts)
# Maybe something like: "Who is the oldest player of all time?"  or "Who played the most games?"  or "Who has the most combined blocks and steals?".
#  Find the player who had the highest PER in one season on the Chicago Bulls
data2.sort(key=lambda x: x[9], reverse=True)
done = False
i = 0
while not done:
    if data2[i][5] == "CHI":
        print(data2[i][2], "had the highest one season PER on the Chicago Bulls with a PER of", data2[i][9])
        done = True
    else:
        i += 1

#7  Big challenge, few points.  Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage?  Which had the best? (2pts)
data2.sort(key=lambda x: x[-1], reverse=True)
top = 100
for i in range(100):
    stored = data2[i][-10]
    if stored < top:
        top = i
print(data2[top][2], "had the lowest free throw percentage of the top 100 single scoring seasons")








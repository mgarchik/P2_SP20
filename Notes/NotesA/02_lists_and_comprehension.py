import random

#  LISTS

my_list = ["Abe", "Bev", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_numlist = [5, 9, 12, 6, 3, -3, 4]

print(my_list[1])  # Bev
print(my_list[-1])  # Gus
print(my_list[1:4])  # Bev to Dan as a list
print(my_list[-3:])  # Eve to Gus as a list


my_copy = my_list  # not a copy, just another link to my original
my_copy.append(("Hal"))
print(my_copy)
print(my_list)

my_copy = my_list[:]  # DO THIS!
my_copy.append("Ida")
print(my_copy)
print(my_list)

my_2d = [["Abe", 8], ["Bev", 7], ["Cam, 4"]]
print(my_2d[1][0])
my_2d[2].append("Wilson")
print(my_2d)

# If in
if "Abe" in my_list:
    print("Abe is there")

if "abe" in my_list:
    print("abe is there")

if random.randrange(10) in [3, 5, 6, 8, 9]:
    print("yay!")


# LIST FUNCTIONS
print(len(my_list))  # returns the length of a list
print(min(my_numlist))  # returns the lowest
print(max(my_numlist))  # highest value
print(max(my_list))  # highest alphabetically
print(sum(my_numlist))

# LIST METHODS
print(my_list.index("Cam"))  # returns the index of the found object
my_list.append("Cam")  # two cams?
print(my_list.index("Cam"))  # only returns the first one
print(my_list.count("Cam"))  # number of Cams
print(my_list.count("Abe"))

my_list.append("Deb")
my_list.sort()  # orders the list
print(my_list)
my_list.reverse()  # reverse the current order
print(my_list)

# manipulating
my_list.pop()  # pops one off the end of the list
print(my_list)
my_person = my_list.pop()
print(my_person)
print(my_list)
front_of_line = my_list.pop(0)
print(front_of_line)
print(my_list)

# destroy an item
del my_list[6]
print(my_list)

# concatenation
first = "Francis"
last = "Parker"
print(first, last)
print(first + last)  # squash

print(my_list + my_numlist)

#  ITERATING THROUGH A LIST
#  FOR EACH LOOP (uses copy)
for name in my_list:
    print(name)

#  INDEX VARIABLE LOOP (directly with list)
for i in range(len(my_list)):
    my_list[i] = my_list[i].lower()
    print(my_list[i])

print(my_list)

#  LIST COMPREHENSIONS
#  [returned_item FOR iterator IN list/range IF filter]

#  make a list from 50 to 100
#  old way
my_list = []
for i in range(50, 101):
    my_list.append(i)

print(my_list)

#  new way
my_list = [x for x in range(50, 101)]  # does same as above
print(my_list)


#  make a list of powers of 2 from 0 to 100
#  old way
my_list = []

for i in range(51):
    my_list.append(2 ** i)

print(my_list)

#  new way
my_list = [2 ** x for x in range(51)]
print(my_list)


#  same list, but filter out any results greater than 100,000
#  old way
my_list = []

for i in range(51):
    if 2 ** i < 100000:
        my_list.append(2 ** i)

print(my_list)

#  new way
my_list = [2 ** x for x in range(51) if 2 ** x < 100000]
print(my_list)

#  roll a single die 100 times and add it to a list
roll = random.randrange(1, 7)

my_list = [random.randrange(1,7) for x in range(101)]
print(my_list)

#  roll two die 100 times and add it to a 2d list:
my_list = [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(101)]
print(my_list) 

#  filter so we only show doubles
my_doubles = [x for x in my_list if x[0] == x[1]]
print(my_doubles)

my_doubles = [x for x in[[random.randrange(1, 7), random.randrange(1, 7)] for x in range(101)] if x[0] == x[1]]
print(my_doubles)


#  Working with strings is similar to lists
first = "Francis"
last = "Parker"
print(first[0])
first = first.upper()
print(first)
print(first + last)
print(last[-3:])

if "Par" in last:
    print("YEP")

for letter in first:
    print(letter)
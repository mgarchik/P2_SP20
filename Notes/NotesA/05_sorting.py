import random

#  Sorting

#  swap values
a = 1
b = 2

temp = a
a = b
b = temp

print(a, b)

# pythonic way
a, b = b, a

# make a random list with 100 numbers 1 to 100 with list comp
iterations = 0

""""
# SELECTION SORT
my_list = [random.randrange(1, 100) for x in range(100)]
my_list_2 = my_list[:]
print(my_list)

for cur_pos in range(len(my_list)):
    min_pos = cur_pos
    for scan_pos in range(cur_pos + 1, len(my_list)):
        iterations += 1
        if my_list[scan_pos] < my_list[min_pos]:
            min_pos = scan_pos
    my_list[cur_pos], my_list[min_pos] = my_list[min_pos], my_list[cur_pos]
print(my_list)
print(iterations)

# INSERTION SORT
iterations = 0
start_time = 0
for key_pos in range(1, len(my_list_2)):
    key_val = my_list_2[key_pos]
    scan_pos = key_pos - 1  # look to dancer on left
    while scan_pos >= 0 and my_list_2[scan_pos] > key_val:
        iterations += 1
        my_list_2[scan_pos + 1] = my_list_2[scan_pos]
        scan_pos -= 1
    my_list_2[scan_pos + 1] = key_val
print(my_list_2)
print(iterations)
"""

# MORE WITH FUNCTIONS
print("Hello", end=" ")  # uses an optional parameter wich has a default value of \n
print("World", end="!\n")


def hello(name, time_of_day="morning"):
    print("Hello", name, "Good", time_of_day)


hello("Matthew", "afternoon")
hello("Owen")  # morning is default value

# Lambda functions (anonymous function on a single line)
double_me = lambda x: x * 2
print(double_me(5))

sum_product = lambda a, b: [a + b, a * b]
print(sum_product(3, 2))

# Real world sorting with python
my_list = [random.randrange(1, 100) for x in range(100)]
print(my_list)

# Sort method (changes the list in place)
my_list.sort()  # default is alphabetically or numerically small to large
print(my_list)

my_list.sort(reverse=True)
print(my_list)

# use a lambda as a key
my_2dlist = [[random.randrange(1, 100), random.randrange(1, 100)] for x in range(100)]
print(my_2dlist)

my_2dlist.sort()
print(my_2dlist)

my_2dlist.sort(key=)
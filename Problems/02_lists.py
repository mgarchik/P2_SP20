import random
# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100
my_list = [x for x in range(101)]
print(my_list)
# b) Make a list of even numbers from 20 to 40
my_list = [x for x in range(20, 41, 2)]
print(my_list)
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_list = [x ** 2 for x in range(101)]
print(my_list)
# d) Make a list of all positive numbers in my_list below.
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
my_pos = [x for x in my_list if x > 1]
print(my_pos)
# PROBLEM 2 (Import the number list - 3pts)
# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
# Print the last 5 numbers in num_list
from number_list import num_list
print(num_list[-5:])

# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
print(max(num_list))
# Find and print the lowest number in num_list (1pt)
print(min(num_list))
# Find and print the average of num_list (2pts)
print(sum(num_list) / len(num_list))
# Remove the lowest number from num_list (2pt)
print(num_list)
del num_list[num_list.index(min(num_list))]
print(num_list)
# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)
num_list.sort()
new_num = num_list[-10:]
print(new_num)
# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?

my_counts = [num_list.count(x) for x in num_list]
print(my_counts)
print(num_list[my_counts.index(max(my_counts))])
# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't
num_list2 = [x for x in num_list]
for i in range(len(num_list2)):
    for j in range(2, num_list2[i]):
        if num_list2[i] % j == 0:
            num_list2[i] = False
            pass
print(num_list2)
primes = [x for x in num_list2 if x]
print(len(primes))


# Find the number of palindromes
# Hint: This may be easier to do with strings
my_strings = [str(x) for x in num_list]
print(my_strings)
palindromes = 0
for i in range(len(my_strings)):
    if my_strings[i][0] == my_strings[i][3] and my_strings[i][1] == my_strings[i][2]:
        palindromes += 1
        print(my_strings[i])
        print(palindromes)


# FORMATTING

import random

# round(n, digits)
print(round(243.4354563, 2))

# format method (a string method)
a = 234.839756
b = 749837465398
print("My number is {}!!".format(a))
print("My numbers are {} and {}".format(a, b))
print("My numbers are {1} and {0}, {1} is my favorite".format(a, b))  # you can specify the order

# justification and spacing
# ^center, >right, <left
for i in range(20):
    c = random.randrange(2000)
    # print("{:6}".format(c))  # six spaces are reserved for the number
    print("**{:^30}**".format(c))

# commas
for i in range(20):
    c = random.randrange(1000000)
    print("${:8,}".format(c))

# precision and datatype (d dec/int, f float, b binary)
for i in range(20):
    c = random.random() * 1000
    print("{:14.3f}".format(c))

for i in range(20):
    c = random.randrange(1000)
    print("{:<10b}".format(c))

# scientific notation
for i in range(20):
    c = random.randrange(1000)
    print("{:.2e}".format(c))
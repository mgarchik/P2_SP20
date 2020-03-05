# Recursion - function calling itself

def f():
    print("f")
    #f ()  # similar to infinite loop


f()  # function calling itself, had to comment out


def g():
    print("g")
    f()


g()  # function calling other functions


#  controlling recursion with def
def controlled(depth, max_depth):
    print("Recursion depth:", depth)
    if depth < max_depth:
        controlled(depth + 1, max_depth)
    print("Recursion depth", depth, "has closed.")


controlled(0, 10)

# Fibonacci
def fibonacci_recursion(n):
    # print("calculating fibonacci for", n)
    # base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # recursive case
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)

for i in range(10):
    print(fibonacci_recursion(i))
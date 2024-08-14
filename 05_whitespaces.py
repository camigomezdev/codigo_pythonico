"""
Whitespace in Expressions and Statements
"""


def function(default_parameter=5):
    pass


# Asignations
x = 3
y = 2

# Priority
# Recommended
if x > 5 and x % 2 == 0:
    print("x is larger than 5 and divisible by 2!")

# Not Recommended
if x>5 and x%2 == 0:
    print("x is larger than 5 and divisible by 2!")


# Definitely do not do this!
if x >5 and x% 2== 0:
    print("x is larger than 5 and divisible by 2!")

# Operations
# Recommended
y = x**2 + 5
z = (x+y) * (x-y)

# Not Recommended
y = x ** 2 + 5
z = (x + y) * (x - y)


# Lists
list[3:4]

# Treat the colon as the operator with lowest priority
list[x+1 : x+2]

# In an extended slice, both colons must be
# surrounded by the same amount of whitespace
list[3:4:5]
list[x+1 : x+2 : x+3]

# The space is omitted if a slice parameter is omitted
list[x+1 : x+2 :]

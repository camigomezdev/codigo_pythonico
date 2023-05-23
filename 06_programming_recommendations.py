"""
Programming Recommendations
"""

## Don’t compare Boolean values to True or False
## using the equivalence operator.

# Not recommended
my_bool = 6 > 5
if my_bool == True:
    print('6 is bigger than 5')


# Recommended
if my_bool:
    print('6 is bigger than 5')


## Use the fact that empty sequences are falsy in if statements.

# Not recommended
my_list = []
if not len(my_list):
    print('List is empty!')

# Recommended
my_list = []
if not my_list:
    print('List is empty!')

## Use is not rather than not ... is in if statements.

# Not recommended
if not x is None:
    print('x exists!')

# Recommended
if x is not None:
    print('x exists!')

## Don’t use if x: when you mean if x is not None:

# Not Recommended
if arg:
    # Do something with arg...
    pass
    

# Recommended
if arg is not None:
    # Do something with arg...
    pass


## Use .startswith() and .endswith() instead of slicing.
word = 'mycat'
# Not recommended
if word[:3] == 'cat':
    print('The word starts with "cat"')

# Recommended
if word.startswith('cat'):
    print('The word starts with "cat"')

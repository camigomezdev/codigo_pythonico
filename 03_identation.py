"""
Identation
"""

# Line Breaks
# Maximum Line Length and Line Breaking
# functions


from turtle import \
    Turtle, \
    color, \
    shape


def long_function(argument_one, argument_two,
                  argument_one_three, argument_four):
    return argument_one


def long_function_two(argument_one,
                      argument_two,
                      argument_one_three,
                      argument_four):
    return argument_one


arg_one, arg_two, arg_three, arg_four = (1, 2, 3, 4)
# Call function
# Recommended
result_1 = long_function(arg_one, arg_two,
                         arg_three, arg_four)

result_2 = long_function(
    arg_one, arg_two, arg_three, arg_four)

# Not Recommended
result_3 = long_function(arg_one, arg_two,
                         arg_three, arg_four)


# Maximum Line Length and Line Breaking
# functions
def long_function(argument_one, argument_two,
                  argument_one_three, argument_four):
    return argument_one


def long_function_two(
        argument_one, argument_two, argument_one_three, argument_four):
    return argument_one


# binary operator
first_variable, second_variable, third_variable = (1, 2, 3)
total = (first_variable
         + second_variable
         - third_variable)

list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]


long_string = """
Use block comments to document a small section of code.
They are useful when you have to write several lines of
code to perform a single action, such as importing data
from a file or updating a database entry. They are important
as they help others understand the purpose and functionality
of a given code block.

PEP 8 provides the following rules for writing block comments:

    Indent block comments to the same level as the code they describe.
    Start each line with a # followed by a single space.
    Separate paragraphs by a line containing a single #.
"""

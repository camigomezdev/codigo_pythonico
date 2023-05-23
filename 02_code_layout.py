"""
Code Layout
"""
# Blank Lines
# Surround top-level functions and classes with two blank lines.


class MyFirstClass:
    # Surround method definitions inside classes with a single blank line.
    def first_method(self):
        return None

    def second_method(self):
        return None


class MySecondClass:
    pass


# Use blank lines sparingly inside functions to show clear steps.
def calculate_variance(number_list):
    sum_list = 0
    for number in number_list:
        sum_list = sum_list + number
    mean = sum_list / len(number_list)

    sum_squares = 0
    for number in number_list:
        sum_squares = sum_squares + number**2
    mean_squares = sum_squares / len(number_list)

    return mean_squares - mean**2

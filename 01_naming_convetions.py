"""
Naming Convetion Examples

module: naming_convetions.py
package: namingconvetions.py
"""

# VARIABLES
# Not recommended
x = "Maria Gomez"
y, z = x.split()

# Recommended
name = "Maria Gomez"
first_name, last_name = name.split()


# CONTANTS
# Recommended
MAX_VALUE = 10
TOTAL = 30


# FUNCTIONS
# Not recommended
def db(x):
    return x * 2


# Recommended
def multiply_by_two(x):
    return x * 2


# CLASSES
class Hero:
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        pass

    def strike_enemy(self, enemy):
        pass


NUMBER_TO_GUESS = "19"
LIVES = 3
lives_played = 0

while lives_played != LIVES:
    number = input("Adivina el numero")

    if number == NUMBER_TO_GUESS:
        print("Ganaste")
        break

    lives_played += 1

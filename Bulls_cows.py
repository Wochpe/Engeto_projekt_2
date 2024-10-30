"""
projekt_2.py: druhý projekt od Engeto Online Python Akademie

autor: Karolína Dvořáková Machová
email: karolin.machova@gmail.com
discord: karolinamach
"""
from random import randint, choice

delim = "-" * 40

def search_for_duplicates(number: str):
    '''
    Verifies presence of duplicates in a string of numbers.
    Returns bool: True for presence at least one duplicite number, False for all unique numbers.
    '''
    num_list = []
    for digit in number:
        if int(digit) not in num_list:
            num_list.append(int(digit))
            duplicates = False
        else:
            duplicates = True
            break
    return duplicates
            

# pozdrav
print("Hi there!")
print(delim)
print("I've generated a random 4 digit number for you."
      "Let's play a bulls and cows game.")
print(delim)

# generování náhodného 4 místného čísla abcd, které nezačíná nulou
all_nubers = []
x = 0
while x < 10:
    all_nubers.append(x)
    x += 1

a = int(randint(1, 9))
all_nubers.remove(a)
b = choice(all_nubers)
all_nubers.remove(b)
c = choice(all_nubers)
all_nubers.remove(c)
d = choice(all_nubers)

win_number = str(a) + str(b) + str(c) +str(d)
win_number = int(win_number)
print(win_number)

# hra


conditions = False
while conditions == False:
    print("Enter a number:")
    delim = "-" * 40
    player_num = input()

## Ověření vstupu od uživatele
    if not player_num.isnumeric():
        print("Incorect input. All symbols must be numeric.")

    elif len(player_num) != 4:
        print("Incorect input lenght. The input has to contain exactly 4 numbers.")
    
    elif search_for_duplicates(player_num):
        print("Incorect input. All 4 numbers must be unique.")
    
    elif player_num[0] == "0":
        print("Incorect input. First number can't be 0.")
    
    else:
        conditions = True

print("Good input.")

"""
projekt_2.py: druhý projekt od Engeto Online Python Akademie

autor: Karolína Dvořáková Machová
email: karolin.machova@gmail.com
discord: karolinamach
"""
from random import randint, choice


# uživatelské funkce a oddělovač
delim = "-" * 40

def search_for_duplicates(number: str) -> bool:
    '''
    Verifies presence of duplicates in an inputed number(str).
    Returns:
        duplicates(bool): True when present at least one duplicate number.
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

def find_bulls_cows(number: str) -> int:
    '''
    Counts the number of correcty guessed numbers.
    Returns:
        bulls(int): The count of all correctly guessed numbers on correct position.
        cows(int): The count of remaining correctly guessed numbers on wrong position.
    '''
    bulls = 0
    cows = 0
    for cipher1, cipher2 in zip(number, win_number):
        if cipher1 == cipher2:
            bulls += 1
    for cipher1 in number:
        if cipher1 in win_number:
            cows += 1
    cows -= bulls
    return bulls, cows
            

# pozdrav
print("Hi there!")
print(delim)
print('''I've generated a random 4 digit number for you."
"Let's play a bulls and cows game.''')
print(delim)

# generování náhodného 4 místného čísla abcd, které nezačíná nulou a je bez duplicit
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

# hra
print("Enter a number:")
print(delim)
n_bulls = 0
n_try = 0
while n_bulls < 4:
    player_num = input(">>> ")
    if not player_num.isnumeric():                          # Ověření číselného vstupu
        print("Incorect input. All symbols must be numeric.")
        print(delim)
    elif len(player_num) != 4:                              # Ověření délky vstupu
        print("Incorect input lenght. The input has to contain exactly 4 numbers.")
        print(delim)
    elif search_for_duplicates(player_num):                         # Ověření jedinečnosti čísel
        print("Incorect input. All 4 numbers must be unique.")
        print(delim)
    elif player_num[0] == "0":                          # Ověření, že nula není na první pozici
        print("Incorect input. First number can't be 0.")
        print(delim)   
    else:
        n_bulls, n_cows = find_bulls_cows(player_num)
        if n_bulls == 1:                            # Podmínky sloužící pouze k vypisování správného tvaru slova bull a cow jejich podle počtu.
            bull_ = "bull"
        else:
            bull_ = "bulls"
        if n_cows == 1:
            cow_ = "cow"
        else:
            cow_ = "cows"
        print(n_bulls, bull_ + ",", n_cows, cow_)
        print(delim)
        n_try += 1                          # Počítá platně zadané pokusy.

else:
    print("Correct, you've guessed the right number\nin", n_try, "guesses!")
    print(delim)
    print("That's amazing!")

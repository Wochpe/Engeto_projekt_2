"""
projekt_2.py: druhý projekt od Engeto Online Python Akademie

autor: Karolína Dvořáková Machová
email: karolin.machova@gmail.com
discord: karolinamach
"""

# Definované funkce a oddělovače
delim1 = 40 * "-"
delim2 = 40 * "="

def evaluate_input(chosen_field:str) -> bool:
    if not chosen_field.isnumeric():
        print("Incorrect input, please enter a number.")
        correct_input = False
    elif int(chosen_field) not in range(1,10):
        print("Incorrect field number, please choose number from 1 to 9.")
        correct_input = False
    else:
        correct_input = True
    return correct_input

def evaluate_empty_field(chosen_field:int,  symbols: list) -> bool:
    x = 1
    for field in symbols:
        if x == chosen_field and symbols[(x-1)] != " ":
            empty = False
            break
        else:
            x += 1
            empty = True
    return empty

def print_playing_fields(chosen_field: int, player_symbol: str, symbols: list):
    x = 1
    for field in symbols:
        if x == chosen_field:
            symbols[(x-1)] = player_symbol
            break
        else:
            x += 1
    print("+---+---+---+")
    print("| " + symbols[0] + " | " + symbols[1] + " | " + symbols[2] + " |")
    print("+---+---+---+")
    print("| " + symbols[3] + " | " + symbols[4] + " | " + symbols[5] + " |")
    print("+---+---+---+")
    print("| " + symbols[6] + " | " + symbols[7] + " | " + symbols[8] + " |")
    print("+---+---+---+")
    return symbols

def evaluete_winner(winning_sequence: list, symbols: list) -> bool:
    row = [list(symbols[:3]), list(symbols[3:6]), list(symbols[5:9])]
    column = [list(symbols[:9:3]), list(symbols[1:9:3]), list(symbols[2:9:3])]
    diagonal = [list(symbols[2:8:2]), list(symbols[:9:4])]
    if winning_sequence in row:
        win = True
    elif winning_sequence in column:
        win = True
    elif winning_sequence in diagonal:
        win = True
    else:
        win = False
    return win

# Hra
## Přivítání
print("Welcome to Tic Tac Toe")
print(delim2)
print('''GAME RULES:
Each player can place one symbol (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
symbols in a:
* horizontal,
* vertical or
* diagonal row''')
print(delim2)
print("Let's start the game")
print(delim1)

## Prázdná hrací plocha
fields= 9 *[" "]
symbols = (print_playing_fields(1, " ", fields))

## Výherní sekvence
win_O = 3 * ["O"]
win_X = 3 * ["X"]

## Vlastní hra
winner = "unknown"
while winner == "unknown":
    print(delim2)
    while not evaluete_winner(win_O, symbols):
        player_O = input("Player O | Please enter your move number: ")
        if not evaluate_input(player_O):
            continue
        elif not evaluate_empty_field(int(player_O), symbols):
            print("This field is already occupied.")
            continue           
        elif not evaluete_winner(win_O, symbols):
            symbols = print_playing_fields(int(player_O), "O", symbols)
            print(delim2)
            break
        else:
            break
    if evaluete_winner(win_O, symbols):
        winner = "Player 0"
        break

            
    while not evaluete_winner(win_X, symbols):
        player_X = input("Player X | Please enter your move number: ")
        if not evaluate_input(player_X):
            continue
        elif not evaluate_empty_field(int(player_X), symbols):
            print("This field is already occupied.")
            continue           
        elif not evaluete_winner(win_X, symbols):
            symbols = (print_playing_fields(int(player_X), "X", symbols))
            print(delim2)
            break
        else:
            break
    if evaluete_winner(win_X, symbols):
        winner = "Player X"
        break
        
print("Congratulation", winner)

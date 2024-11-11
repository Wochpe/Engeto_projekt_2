"""
projekt_2.py: druhý projekt od Engeto Online Python Akademie

autor: Karolína Dvořáková Machová
email: karolin.machova@gmail.com
discord: karolinamach
"""

# Definované funkce a oddělovače
delim1 = 44 * "-"
delim2 = 44 * "="

def evaluate_input(chosen_field:str) -> bool:
    '''
    Returns True if string player input is number between 1 and 9, False otherwise.
    '''
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
    '''
    Returns True if field is empty, False otherwise.
    Args:
        chosen_field(int): Number of the field chosen by player.
        symbols(list): List of current symbols on the playing field.
    '''
    x = 1
    for field in symbols:
        if x == chosen_field and symbols[(x-1)] != " ":
            empty = False
            break
        else:
            x += 1
            empty = True
    return empty

def print_playing_fields(chosen_field: int, player_symbol: str, symbols: list):                 # Tato funkce by mohla být rozdělena na dvě.
    '''
    Prints playing field with the last symbol added.
    Args:
        chosen_field(int): Number of a field chosen by the player.
        player_symbol(str): A symbol of the current player ("O"/"X").
        symbols(list): List of current symbols present on the playing field.
    Returns:
        symbols(list): Apdated list of symbols.
    '''    
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
    '''
    Compares possible winning sequences with the list of symbols.
    Returns True if they are the same, False otherwise.
    Args:
        winning_sequence(list): List of 3 identical symbols ("O"/"X").
        symbols(list): List of current symbols on the playing field.
    '''

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
winner = "Unknown"
while winner == "Unknown":                          # Hlavní smyčka, která reprezentuje jedno kolo (tahy 2 hráčů).
    while not evaluete_winner(win_O, symbols):                           # Vnitřní smyčka prvního hráče "O".
        print(delim2)
        player_O = input("Player O | Please enter your move number: ")
        print(delim2)
        if not evaluate_input(player_O):                            # Pokud nezadán správný vstup, smyčka se ptá znovu stejného hráče.
            continue
        elif not evaluate_empty_field(int(player_O), symbols):                          # Pokud nezadáno prázdné pole, smyčka se ptá znovu stejného hráče.
            print("This field is already occupied.")
            continue           
        elif not evaluete_winner(win_O, symbols):                           # Pokud není někde v poli výherní sekvence (z předchozího tahu). 
            symbols = print_playing_fields(int(player_O), "O", symbols)                         # Zapíše do pole nový symbol a ukončí vnitřní smyčku.
            break
        else:                         # Pokud by vítězná sekvence byla přítomná, ukončí vnitřní smyčku.
            break
    if evaluete_winner(win_O, symbols):                       # Pokud došlo k ukončení vnitřní smyčky kvůli výhře, zapíše výherce a ukončí vnější smyčku.
        winner = "Player 0"
        break
    elif " " not in symbols:                          # Pokud už není volné pole, přepíše podmínku vnější smyčka nechá ji tím doběhnout.
        winner = "None"
        continue

            
    while not evaluete_winner(win_X, symbols):                        # Vnitřní smyčka druhého hráče "X".
        print(delim2)
        player_X = input("Player X | Please enter your move number: ")
        print(delim2)
        if not evaluate_input(player_X):
            continue
        elif not evaluate_empty_field(int(player_X), symbols):
            print("This field is already occupied.")
            continue           
        elif not evaluete_winner(win_X, symbols):
            symbols = (print_playing_fields(int(player_X), "X", symbols))
            break
        else:
            break
    if evaluete_winner(win_X, symbols):
        winner = "Player X"
        break
    elif " " not in symbols:
        winner = "None"
        continue
else:                           # Pokud vnější smyčka doběhne (pouze při remíze), vypíše hlášku a ukončí program.
    print(delim2)
    print("It's a draw!")
    print(delim2)
    exit()

print(delim2)
print("Congratulation, the", winner, "won!")                    # Pokud je vnější smyčka přerušena (výhrou), vypíše vítěze.
print(delim2)            

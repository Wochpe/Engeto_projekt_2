"""
projekt_2.py: druhý projekt od Engeto Online Python Akademie

autor: Karolína Dvořáková Machová
email: karolin.machova@gmail.com
discord: karolinamach
"""

# Definované funkce a oddělovače
delim1 = 40 * "-"
delim2 = 40 * "="

def print_playing_field(chosen_fied: int, player_symbol: str):
    if chosen_fied not in range(1,10):
        print("Incorrect field number, please choose number from 1 to 9.")
    else:
        x = 1
        for field in mark:
            if x == chosen_fied and mark[(x-1)] != " ":
                print("This field is already occupied.")
                break
            elif x == chosen_fied:
                mark[(x-1)] = player_symbol
                break
            else:
                x += 1
        print("+---+---+---+")
        print("| " + mark[0] + " | " + mark[1] + " | " + mark[2] + " |")
        print("+---+---+---+")
        print("| " + mark[3] + " | " + mark[4] + " | " + mark[5] + " |")
        print("+---+---+---+")
        print("| " + mark[6] + " | " + mark[7] + " | " + mark[8] + " |")
        print("+---+---+---+")
    return mark

# Hra
## Přivítání
print("Welcome to Tic Tac Toe")
print(delim2)
print('''GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row''')
print(delim2)
print("Let's start the game")
print(delim1)

## Prázdná hrací plocha
mark = 9 *[" "]
mark = (print_playing_field(1, " "))

## Vlastní hra
win_O = 3 * ["O"]
win_X = 3 * ["X"]
row = mark[:2] or mark[3:6] or mark[5:9]
column = mark[:9, 3] or mark[1:9, 3] or mark[2:9, 3]
diagonal = mark[2, 4, 6] or mark[1, 4, 8]
winner = "unknown"
while winner == "unknown":
    if win_O != row or column or diagonal:
        print(delim2)
        player_O = int(input("Player O | Please enter your move number: "))
        mark = (print_playing_field(player_O, "O"))
        print(delim2)
    else:
        winner = "Player 0"
        break
    if win_X != row or column or diagonal:
        print(delim2)
        player_X = int(input("Player X | Please enter your move number: "))
        mark = (print_playing_field(player_X, "X"))
        print(delim2)
    else:
        winner = "Player X"
        break
print("Congratulation", winner)


# player_X = input("Player X | Please enter your move number: ")
# print(delim2)
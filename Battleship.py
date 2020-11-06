'''
Asher Forman
Battleship
10/16/20
'''
from colored import fg, attr
import time
player1_team = " "
player2_team = " "
win_factor = False

board_player_1 = [
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "]
]
board_player_2 = [
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "]
]

words_To_numbers = {
    "A": 0,
    "a": 0,
    "B": 1,
    "b": 1,
    "C": 2,
    "c": 2,
    "D": 3,
    "d": 3,
    "E": 4,
    "e": 4
}

def welcome():
    global player1_team
    global player2_team
    print("Welcome to Battleship!")
    print("%s                                  )___(                             \n"
           "                            _______/__/_                            \n"
           "                   ___     /===========|   ___                      \n"
           "  ____       __   [\\\]___/____________|__[///]   __                \n"
           "  \   \_____[\\]__/___________________________\__[//]___            \n"
           "   \ Asher's Battleship                                 |           \n"
           "    \                                                  /            \n" 
           " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       %s" % (fg('dark_orange'), attr(0)))
    player1_team = input("Type C to be the Confederates or U to be the Union: ")
    upper_case_choose_team = player1_team.upper()

    if upper_case_choose_team == "C":
        player2_team = "U"
        print("Player 1 is the Confederates and Player 2 is the Union!")
    else:
        player2_team = "C"
        print("Player 1 is the Union and Player 2 is the Confederates!")


def draw_player1_board():
    for i in range(5):
        for j in range(5):
            board_player_1[i][j] = "~"
    for i in range(5):
        print(board_player_1[i])


def draw_player2_board():
    for i in range(5):
        for j in range(5):
            board_player_2[i][j] = "~"
    for i in range(5):
        print(board_player_2[i])


def print_player1_board():
    print(f'''%s
        0 1 2 3 4
       ___________
    A | {board_player_1[words_To_numbers['A']][0]}|{board_player_1[words_To_numbers['A']][1]}|{board_player_1[words_To_numbers['A']][2]}|{board_player_1[words_To_numbers['A']][3]}|{board_player_1[words_To_numbers['A']][4]} |
      | ~~~~~~~~~~ 
    B | {board_player_1[words_To_numbers['B']][0]}|{board_player_1[words_To_numbers['B']][1]}|{board_player_1[words_To_numbers['B']][2]}|{board_player_1[words_To_numbers['B']][3]}|{board_player_1[words_To_numbers['B']][4]} |
      | ~~~~~~~~~~                                  
    C | {board_player_1[words_To_numbers['C']][0]}|{board_player_1[words_To_numbers['C']][1]}|{board_player_1[words_To_numbers['C']][2]}|{board_player_1[words_To_numbers['C']][3]}|{board_player_1[words_To_numbers['C']][4]} |
      | ~~~~~~~~~~ 
    D | {board_player_1[words_To_numbers['D']][0]}|{board_player_1[words_To_numbers['D']][1]}|{board_player_1[words_To_numbers['D']][2]}|{board_player_1[words_To_numbers['D']][3]}|{board_player_1[words_To_numbers['D']][4]} |
      | ~~~~~~~~~~
    E | {board_player_1[words_To_numbers['E']][0]}|{board_player_1[words_To_numbers['E']][1]}|{board_player_1[words_To_numbers['E']][2]}|{board_player_1[words_To_numbers['E']][3]}|{board_player_1[words_To_numbers['E']][4]} |
       ___________
    %s''' % (fg(1), attr(0)))
def print_player2_board():
    print(f'''%s
        0 1 2 3 4
       ___________
    A | {board_player_2[words_To_numbers['A']][0]}|{board_player_2[words_To_numbers['A']][1]}|{board_player_2[words_To_numbers['A']][2]}|{board_player_2[words_To_numbers['A']][3]}|{board_player_2[words_To_numbers['A']][4]} |
      | ~~~~~~~~~~ 
    B | {board_player_2[words_To_numbers['B']][0]}|{board_player_2[words_To_numbers['B']][1]}|{board_player_2[words_To_numbers['B']][2]}|{board_player_2[words_To_numbers['B']][3]}|{board_player_2[words_To_numbers['B']][4]} |
      | ~~~~~~~~~~                                  
    C | {board_player_2[words_To_numbers['C']][0]}|{board_player_2[words_To_numbers['C']][1]}|{board_player_2[words_To_numbers['C']][2]}|{board_player_2[words_To_numbers['C']][3]}|{board_player_2[words_To_numbers['C']][4]} |
      | ~~~~~~~~~~ 
    D | {board_player_2[words_To_numbers['D']][0]}|{board_player_2[words_To_numbers['D']][1]}|{board_player_2[words_To_numbers['D']][2]}|{board_player_2[words_To_numbers['D']][3]}|{board_player_2[words_To_numbers['D']][4]} |
      | ~~~~~~~~~~
    E | {board_player_2[words_To_numbers['E']][0]}|{board_player_2[words_To_numbers['E']][1]}|{board_player_2[words_To_numbers['E']][2]}|{board_player_2[words_To_numbers['E']][3]}|{board_player_2[words_To_numbers['E']][4]} |
       ___________
    %s'''% (fg('sky_blue_3'), attr(0)))


def player_1_place_ships():
    global player1_team
    place_ships_row = input("Player 1, choose your row: ")
    place_ships_col = input("Player 1, choose your column: ")


    letter_place_ships_row = words_To_numbers[place_ships_row]
    int_place_ships_col = int(place_ships_col)


    board_player_1[letter_place_ships_row][int_place_ships_col] = player1_team.upper()


    print_player1_board()



def player_2_place_ships():
    global player2_team
    place_ships_row = input("Player 2, choose your row: ")
    place_ships_col = input("Player 2, choose your column: ")

    letter_place_ships_row = words_To_numbers[place_ships_row]
    int_place_ships_col = int(place_ships_col)


    board_player_2[letter_place_ships_row][int_place_ships_col] = player2_team.upper()

    print_player2_board()

def player_1_turn():
    global player2_team
    fire_opposing_ships_row = input("Player 1, guess a row to sink Player 2's ship: ")
    fire_opposing_ships_col = input("Player 1, guess a col to sink Player 2's ship: ")

    letter_fire_opposing_ships_row = words_To_numbers[fire_opposing_ships_row]
    int_fire_opposing_ships_col = int(fire_opposing_ships_col)

    if board_player_2[letter_fire_opposing_ships_row][int_fire_opposing_ships_col] == player2_team:
        board_player_2[letter_fire_opposing_ships_row][int_fire_opposing_ships_col] = "S"
        print("Player 1 hit Player 2's battleship! Look at that explosion!")
        print("%s             __,-~~/~    `---.            \n"
              "             _/_,---(      ,    )           \n"
              "         __ /        <    /   )  \___       \n"
              "  --===;;;'====------------------===;;;==   \n"
              "            \/      ~~~~~\~~)~/             \n"
              "            (_ (   \  (     >    \)         \n"
              "             \_( _ <         >_>'           \n"
              "                ~ `-i' ::>|--               \n"
              "                    I;|.|.|                 \n"
              "                 __<|i::|i|____  %s" % (fg('grey_58'), attr(0)))
        time.sleep(2)
    else:
        print("Player 1 missed and hit the water!")
        print("%s  _      _      _      _      _      _      _      _  \n"
              "  )`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_ %s" % (fg('deep_sky_blue_4c'), attr(0)))
        time.sleep(2)
        board_player_2[letter_fire_opposing_ships_row][int_fire_opposing_ships_col] = "M"



def player_2_turn():
    global player1_team
    fire_opposing_ships_row = input("Player 2, guess a row to sink Player 1's ship: ")
    fire_opposing_ships_col = input("Player 2, guess a col to sink Player 1's ship: ")

    letter_fire_opposing_ships_row = words_To_numbers[fire_opposing_ships_row]
    int_fire_opposing_ships_col = int(fire_opposing_ships_col)

    if board_player_1[letter_fire_opposing_ships_row][int_fire_opposing_ships_col] == player1_team:
        board_player_1[letter_fire_opposing_ships_row][int_fire_opposing_ships_col] = "S"
        print("Player 2 hit Player 1's battleship! Look at that explosion!")
        print("%s             __,-~~/~    `---.            \n"
              "             _/_,---(      ,    )           \n"
              "         __ /        <    /   )  \___       \n"
              "  --===;;;'====------------------===;;;==   \n"
              "            \/      ~~~~~\~~)~/             \n"
              "            (_ (   \  (     >    \)         \n"
              "             \_( _ <         >_>'           \n"
              "                ~ `-i' ::>|--               \n"
              "                    I;|.|.|                 \n"
              "                 __<|i::|i|____  %s" % (fg('grey_58'), attr(0)))
        time.sleep(2)
    else:
        print("Player 2 missed and hit the water!")
        print("%s  _      _      _      _      _      _      _      _  \n"
              "  )`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_ %s" % (fg('deep_sky_blue_4c'), attr(0)))
        time.sleep(2)
        board_player_1[letter_fire_opposing_ships_row][int_fire_opposing_ships_col] = "M"


def clear_board_p1_p2():
    global board_player_1
    global board_player_2
    board_player_1 = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "]
    ]
    board_player_2 = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "]
    ]



def didIWin():
    global win_factor
    for row in board_player_1:
        if row.count("S") == 3:
            win_factor = True
    for row in board_player_2:
        if row.count("S") == 3:
            win_factor = True


def continue_playing():
    play_continue = input("Type c to cover your board: ")
    upper_case_play_continue = play_continue.upper()
    if upper_case_play_continue == "C":
        print("\n" * 15)
    else:
        continue_playing()


def ship_placement():
    print_player1_board()
    for i in range(3):
        player_1_place_ships()
    print("\n" * 15)
    print_player2_board()
    for i in range(3):
        player_2_place_ships()
    print("\n" * 15)


def game_play():
    welcome()
    ship_placement()
    global win_factor
    while win_factor == False:
        player_1_turn()
        print_player1_board()
        didIWin()
        if win_factor == True:
            print("Congratulations, Player 1 won the Game!")
            print("%s                                            _         \n"
                  "                                           | |        \n"
                  "             ___ ___  _ __   __ _ _ __ __ _| |_ ___   \n"
                  "            / __/ _ \| '_ \ / _` | '__/ _` | __/ __|  \n"
                  "           | (_| (_) | | | | (_| | | | (_| | |_\__ \  \n"
                  "            \___\___/|_| |_|\__, |_|  \__,_|\__|___/  \n"
                  "                             __/ |                    \n"
                  "                            |___/       %s" % (fg('spring_green_2b'), attr(0)))
            play_again_end = input("Type y to play again or n to end: ")
            upper_case_play_again_end = play_again_end.upper()
            if upper_case_play_again_end == "Y":
                clear_board_p1_p2()
                win_factor = False
                game_play()
            else:
                print("Game Over! Player 1 Won!")
                exit()
        continue_playing()
        player_2_turn()
        print_player2_board()
        didIWin()
        if win_factor == True:
            print("Congratulations, Player 2 won the Game!")
            print("%s                                            _         \n"
                  "                                           | |        \n"
                  "             ___ ___  _ __   __ _ _ __ __ _| |_ ___   \n"
                  "            / __/ _ \| '_ \ / _` | '__/ _` | __/ __|  \n"
                  "           | (_| (_) | | | | (_| | | | (_| | |_\__ \  \n"
                  "            \___\___/|_| |_|\__, |_|  \__,_|\__|___/  \n"
                  "                             __/ |                    \n"
                  "                            |___/       %s" % (fg('blue_violet'), attr(0)))
            play_again_end = input("Type y to play again or n to end: ")
            upper_case_play_again_end = play_again_end.upper()
            if upper_case_play_again_end == "Y":
                clear_board_p1_p2()
                win_factor = False
                game_play()
            else:
                print("Game Over! Player 2 Won!")
                exit()
        continue_playing()
game_play()



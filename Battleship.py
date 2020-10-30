'''
Asher Forman
Battleship
10/16/20
'''
player1_team = " "
player2_team = " "
win_factor = False
from colored import fg, bg, attr

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

def welcome():
    global player1_team
    global player2_team
    print("Welcome to Battleship!")
    print( "                                  )___(                             \n"
           "                            _______/__/_                            \n"
           "                   ___     /===========|   ___                      \n"
           "  ____       __   [\\\]___/____________|__[///]   __                \n"
           "  \   \_____[\\]__/___________________________\__[//]___            \n"
           "   \40A                                                 |           \n"
           "    \                                                  /            \n" 
           " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       ")
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
    0 | {board_player_1[0][0]}|{board_player_1[0][1]}|{board_player_1[0][2]}|{board_player_1[0][3]}|{board_player_1[0][4]} |
      | ~~~~~~~~~~ 
    1 | {board_player_1[1][0]}|{board_player_1[1][1]}|{board_player_1[1][2]}|{board_player_1[1][3]}|{board_player_1[1][4]} |
      | ~~~~~~~~~~                                  
    2 | {board_player_1[2][0]}|{board_player_1[2][1]}|{board_player_1[2][2]}|{board_player_1[2][3]}|{board_player_1[2][4]} |
      | ~~~~~~~~~~ 
    3 | {board_player_1[3][0]}|{board_player_1[3][1]}|{board_player_1[3][2]}|{board_player_1[3][3]}|{board_player_1[3][4]} |
      | ~~~~~~~~~~
    4 | {board_player_1[4][0]}|{board_player_1[4][1]}|{board_player_1[4][2]}|{board_player_1[4][3]}|{board_player_1[4][4]} |
       ___________
    %s''' % (fg(1), attr(0)))
def print_player2_board():
    print(f'''%s
        0 1 2 3 4
       ___________
    0 | {board_player_2[0][0]}|{board_player_2[0][1]}|{board_player_2[0][2]}|{board_player_2[0][3]}|{board_player_2[0][4]} |
      | ~~~~~~~~~~ 
    1 | {board_player_2[1][0]}|{board_player_2[1][1]}|{board_player_2[1][2]}|{board_player_2[1][3]}|{board_player_2[1][4]} |
      | ~~~~~~~~~~                                  
    2 | {board_player_2[2][0]}|{board_player_2[2][1]}|{board_player_2[2][2]}|{board_player_2[2][3]}|{board_player_2[2][4]} |
      | ~~~~~~~~~~ 
    3 | {board_player_2[3][0]}|{board_player_2[3][1]}|{board_player_2[3][2]}|{board_player_2[3][3]}|{board_player_2[3][4]} |
      | ~~~~~~~~~~
    4 | {board_player_2[4][0]}|{board_player_2[4][1]}|{board_player_2[4][2]}|{board_player_2[4][3]}|{board_player_2[4][4]} |
       ___________
    %s'''% (fg('sky_blue_3'), attr(0)))


def player_1_place_ships():
    global player1_team
    place_ships_row = input("Player 1, choose your row: ")
    place_ships_col = input("Player 1, choose your column: ")

    int_place_ships_row = int(place_ships_row)
    int_place_ships_col = int(place_ships_col)


    print(f'Player 1 picked row {int_place_ships_row} and column {int_place_ships_col}')

    board_player_1[int_place_ships_row][int_place_ships_col] = player1_team

    print_player1_board()



def player_2_place_ships():
    global player2_team
    place_ships_row = input("Player 2, choose your row: ")
    place_ships_col = input("Player 2, choose your column: ")

    int_place_ships_row = int(place_ships_row)
    int_place_ships_col = int(place_ships_col)


    print(f'Player 2 picked row {int_place_ships_row} and column {int_place_ships_col}')

    board_player_2[int_place_ships_row][int_place_ships_col] = player2_team

    print_player2_board()

def player_1_turn():
    global player2_team
    fire_opposing_ships_row = input("Player 1, guess a row to sink Player 2's ship: ")
    fire_opposing_ships_col = input("Player 1, guess a col to sink Player 2's ship: ")

    int_fire_opposing_ships_row = int(fire_opposing_ships_row)
    int_fire_opposing_ships_col = int(fire_opposing_ships_col)

    print(f'Player 1 picked row {int_fire_opposing_ships_row} and column {int_fire_opposing_ships_col}')


    if board_player_2[int_fire_opposing_ships_row][int_fire_opposing_ships_col] == player2_team:
        board_player_2[int_fire_opposing_ships_row][int_fire_opposing_ships_col] = "S"
        print("Player 1 hit Player 2's battleship!")
    else:
        print("Player 1 missed and hit the water!")
        board_player_2[int_fire_opposing_ships_row][int_fire_opposing_ships_col] = "M"



def player_2_turn():
    global player1_team
    fire_opposing_ships_row = input("Player 2, guess a row to sink Player 1's ship: ")
    fire_opposing_ships_col = input("Player 2, guess a col to sink Player 1's ship: ")

    int_fire_opposing_ships_row = int(fire_opposing_ships_row)
    int_fire_opposing_ships_col = int(fire_opposing_ships_col)

    print(f'Player 2 picked row {int_fire_opposing_ships_row} and column {int_fire_opposing_ships_col}')

    if board_player_1[int_fire_opposing_ships_row][int_fire_opposing_ships_col] == player1_team:
        board_player_1[int_fire_opposing_ships_row][int_fire_opposing_ships_col] = "S"
        print("Player 2 hit Player 1's battleship!")
    else:
        print("Player 2 missed and hit the water!")
        board_player_1[int_fire_opposing_ships_row][int_fire_opposing_ships_col] = "M"


def clear_board_p1_p2():
    global board_player_1
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
        print("\n" * 10)
    else:
        continue_playing()


def ship_placement():
    print_player1_board()
    for i in range(3):
        player_1_place_ships()
    print("\n" * 10)
    print_player2_board()
    for i in range(3):
        player_2_place_ships()
    print("\n" * 10)


def game_play():
    welcome()
    ship_placement()
    global win_factor
    while win_factor == False:
        player_1_turn()
        print_player1_board()
        didIWin()
        continue_playing()
        if win_factor == True:
            print("Congratulations, Player 1 won the Game!")
            print("                                            _         \n"
                  "                                           | |        \n"
                  "             ___ ___  _ __   __ _ _ __ __ _| |_ ___   \n"
                  "            / __/ _ \| '_ \ / _` | '__/ _` | __/ __|  \n"
                  "           | (_| (_) | | | | (_| | | | (_| | |_\__ \  \n"
                  "            \___\___/|_| |_|\__, |_|  \__,_|\__|___/  \n"
                  "                             __/ |                    \n"
                  "                            |___/       ")
            play_again_end = input("Type y to play again or n to end: ")
            upper_case_play_again_end = play_again_end.upper()
            if upper_case_play_again_end == "Y":
                clear_board_p1_p2()
                game_play()
            else:
                print("Game Over!")
                exit()
        player_2_turn()
        print_player2_board()
        didIWin()
        continue_playing()
        if win_factor == True:
            print("Congratulations, Player 2 won the Game!")
            print("                                            _         \n"
                  "                                           | |        \n"
                  "             ___ ___  _ __   __ _ _ __ __ _| |_ ___   \n"
                  "            / __/ _ \| '_ \ / _` | '__/ _` | __/ __|  \n"
                  "           | (_| (_) | | | | (_| | | | (_| | |_\__ \  \n"
                  "            \___\___/|_| |_|\__, |_|  \__,_|\__|___/  \n"
                  "                             __/ |                    \n"
                  "                            |___/       ")
            play_again_end = input("Type y to play again or n to end: ")
            upper_case_play_again_end = play_again_end.upper()
            if upper_case_play_again_end == "Y":
                clear_board_p1_p2()
                game_play()
            else:
                print("Game Over!")
                exit()
game_play()



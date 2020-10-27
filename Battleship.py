'''
Asher Forman
Battleship
10/16/20
'''
import numpy
player1_team = " "
player2_team = " "
win_factor = False

board_player_1 = [
    ["Sunk", " ", " ", " ", " "],
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


def player_1_place_ships():
    global player1_team
    place_ships_row = input("Player 1, choose your row: ")
    place_ships_col = input("Player 1, choose your column: ")

    int_place_ships_row = int(place_ships_row)
    int_place_ships_col = int(place_ships_col)


    print(f'Player 1 picked row {int_place_ships_row} and column {int_place_ships_col}')

    board_player_1[int_place_ships_row][int_place_ships_col] = player1_team

    for i in range(5):
        print(board_player_1[i])



def player_2_place_ships():
    global player2_team
    place_ships_row = input("Player 2, choose your row: ")
    place_ships_col = input("Player 2, choose your column: ")

    int_place_ships_row = int(place_ships_row)
    int_place_ships_col = int(place_ships_col)


    print(f'Player 2 picked row {int_place_ships_row} and column {int_place_ships_col}')

    board_player_2[int_place_ships_row][int_place_ships_col] = player2_team

    for i in range(5):
        print(board_player_2[i])

def player_1_turn():
    global player2_team
    fire_opposing_ships_row = input("Player 1, guess a row to sink Player 2's ship: ")
    fire_opposing_ships_col = input("Player 1, guess a col to sink Player 2's ship: ")

    int_fire_opposing_ships_row = int(fire_opposing_ships_row)
    int_fire_opposing_ships_col = int(fire_opposing_ships_col)

    print(f'Player 1 picked row {int_fire_opposing_ships_row} and column {int_fire_opposing_ships_col}')


    if board_player_2[int_fire_opposing_ships_row][int_fire_opposing_ships_col] == player2_team:
        board_player_2[int_fire_opposing_ships_row][int_fire_opposing_ships_col] = "Sunk"
        print("Player 1 hit Player 2's battleship!")
    else:
        print("Player 1 missed and hit the water!")
        board_player_2[int_fire_opposing_ships_row][int_fire_opposing_ships_col] = "Miss"




def player_2_turn():
    global player1_team
    fire_opposing_ships_row = input("Player 2, guess a row to sink Player 1's ship: ")
    fire_opposing_ships_col = input("Player 2, guess a col to sink Player 1's ship: ")

    int_fire_opposing_ships_row = int(fire_opposing_ships_row)
    int_fire_opposing_ships_col = int(fire_opposing_ships_col)

    print(f'Player 2 picked row {int_fire_opposing_ships_row} and column {int_fire_opposing_ships_col}')

    if board_player_1[int_fire_opposing_ships_row][int_fire_opposing_ships_col] == player1_team:
        board_player_1[int_fire_opposing_ships_row][int_fire_opposing_ships_col] = "Sunk"
        print("Player 2 hit Player 1's battleship!")
    else:
        print("Player 2 missed and hit the water!")
        board_player_1[int_fire_opposing_ships_row][int_fire_opposing_ships_col] = "Miss"


    for i in range(5):
        print(board_player_1[i])


def didIWin():
    global win_factor
    for row in board_player_1:
        if row.count("Sunk") == 3:
            win_factor = True
    for row in board_player_2:
        if row.count("Sunk") == 3:
            win_factor = True





def ship_placement():
    draw_player1_board()
    for i in range(3):
        player_1_place_ships()
    print("\n" * 10)
    draw_player2_board()
    for i in range(3):
        player_2_place_ships()
    print("\n" * 10)


def game_play():
    welcome()
    ship_placement()
    global win_factor
    while win_factor == False:
        player_1_turn()
        didIWin()
        if win_factor == True:
            print("Congratulations, Player 1 won the Game!")
            print("(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)")
        player_2_turn()
        didIWin()
        if win_factor == True:
            print("Congratulations, Player 1 won the Game!")
            print("(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)")


game_play()





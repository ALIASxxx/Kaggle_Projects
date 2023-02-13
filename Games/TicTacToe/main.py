# WHAT NEEDS TO HAPPEN
# 1) Print a board
# 2) Take in player input
# 3) Place input on the board
# 4) Check if the game is won,tied, lost, or ongoing.
# 5) Repeat 1,2,3,4 in until the game has been won or tied.
# 6) Ask if players they want to play again
import random


def display_board(board1):
    print('\n' * 10)
    print('   |   |')
    print(' ' + board1[1] + ' | ' + board1[2] + ' | ' + board1[3])
    print('   |   |')
    print('___________')
    print('   |   |')
    print(' ' + board1[4] + ' | ' + board1[5] + ' | ' + board1[6])
    print('   |   |')
    print('___________')
    print('   |   |')
    print(' ' + board1[7] + ' | ' + board1[8] + ' | ' + board1[9])
    print('   |   |')


def choose_marker():
    p1 = ''
    while p1 not in ['X', 'O']:
        p1 = input('Player 1: Would you like to be X or O?').upper()

    if p1 == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def first_turn():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, pos):
    return board[pos] == ' '


def full_board_check(board):
    for x in range(1, 10):
        if space_check(board, x):
            return False
    return True


def place_marker(board, marker, position):
    board[position] = marker


def player_choice(board, marker):
    position1 = 0
    while position1 not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position1):
        position1 = int(input(marker + ": Choose a position (1-9) "))
    return position1


def replay():
    choice = input('Play again? Enter Yes or No').lower()
    return choice == 'yes'


def check_endgame(board, mark):
    # Check each row, column, diagonal to see if they share same marker
    if (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or \
            (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or \
            (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or \
            (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark):
        print(mark + ' wins!')
        return True
    return False


print("Welcome to Tic Tac Toe")
print('****************************')
print('This is the position corresponding with each section of the Tic Tac Toe board:')
print('1|2|3')
print('_____')
print('4|5|6')
print('_____')
print('7|8|9')

while True:

    # PLAY GAME

    # SET EVERYTHING UP (board, whos first, choose markers X O)
    board = [' '] * 10

    player1_marker, player2_marker = choose_marker()
    turn = first_turn()

    endgame = check_endgame(board, '#')
    while not endgame:
        # Player 1's turn
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board, player1_marker)
            place_marker(board, player1_marker, position)
            turn = 'Player 2'
            if check_endgame(board, player1_marker):
                display_board(board)
                print("PLAYER 1 HAS WON!!!")
                break
            elif full_board_check(board):
                print("TIE GAME!")
                break

        # Player 2's turn
        if turn == 'Player 2':
            display_board(board)
            position = player_choice(board, player2_marker)
            place_marker(board, player2_marker, position)
            turn = 'Player 1'
            if check_endgame(board, player2_marker):
                display_board(board)
                print("PLAYER 2 HAS WON!!!")
                break
            elif full_board_check(board):
                print("TIE GAME!")
                break

    if not replay():
        break

import random

from pip.backwardcompat import raw_input

board = ['', '', '', '', '', '', '', '', '', '']


def game_board():  # print the board
    print(' ----------- ')
    print("|", "", board[0], "|", "", board[1], "|", "", board[2], "|", )
    print(' ----------- ')
    print("|", "", board[3], "|", "", board[4], "|", "", board[5], "|")
    print(' ----------- ')
    print("|", "", board[6], "|", "", board[7], "|", "", board[8], "|")
    print(' ----------- ')


def check(char, spot1, spot2, spot3):                                      # Function to check the 3 spots
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True


def checkall(char):                                                         #Function to check all the combinations
    if check('char', 0, 1, 2):
        return True
    if check('char', 3, 4, 5):
        return True
    if check('char', 6, 7, 8):
        return True

    if check('char', 0, 3, 6):
        return True
    if check('char', 1, 4, 7):
        return True
    if check('char', 2, 5, 8):
        return True

    if check('char', 0, 4, 8):
        return True
    if check('char', 2, 4, 6):
        return True

count=0
while count<10:
    while True:
        input1 = raw_input("Enter the spot:")  # takes input
        input1 = int(input1)

        if board[input1] != 'X' and board[input1] != 'O':
            board[input1] = 'X'

            if checkall('X') == True:                          # Winner check
                print("X wins. Here X means Player")
                break

            while True and count<9:
                random.seed()                           # Generating random number
                computer = random.randint(0, 8)

                if board[computer] != 'O' and board[computer] != 'X':
                    board[computer] = 'O'

                    if checkall('O')==True:                      # Winner check
                        print("O wins")
                        break

                    break

        else:
            print('spot already taken or Invalid spot')
        print(game_board())

count=count+1
# Tic Tac Toe with MinMax Algorithm
# Max will try to maximize utility
# Min will try to minimize user utility to win
# time complexity: O(b^d)

import random

board = [' ' for i in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos == ' ']


def printBoard(board):
    # Displays the board, ignore index 0
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(board, letter):
    return (board[7] == letter and board[8] == letter and board[9] == letter) or \
           (board[4] == letter and board[5] == letter and board[6] == letter) or \
           (board[1] == letter and board[2] == letter and board[3] == letter) or \
           (board[1] == letter and board[4] == letter and board[7] == letter) or \
           (board[2] == letter and board[5] == letter and board[8] == letter) or \
           (board[3] == letter and board[6] == letter and board[9] == letter) or \
           (board[1] == letter and board[5] == letter and board[9] == letter) or \
           (board[3] == letter and board[5] == letter and board[7] == letter)


def playerMove():
    # Takes the input from user and validates users input
    run = True
    while run:
        try:
            move = int(input('Please select a position to place \'X\' (1-9): '))
            if isinstance(move, str):
                print('Enter a valid number..')
            if 0 < move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def compMove():
    # 1. winning move
    # 2. Block move, if user gets benefited
    # 3. move at corner
    # 4. move at center
    # 5. move at edge
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    # First way: check if computer can win or no, if not then computer tries to block users move, so that he cannot win
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    if board[1] == 'X' or board[3] == 'X' or board[7] == 'X' or board[9] == 'X':
        if 5 in possibleMoves:
            move = 5
            return move

    edgesOpen = []

    if (board[1] == 'X' and board[9] == 'X') or (board[3] == 'X' and board[7] == 'X'):
        for i in possibleMoves:
            if i in [2, 4, 6, 8]:
                edgesOpen.append(i)

    # randomly select a corner to move Into
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

    # Same code also for edges
    cornersOpen = []

    # Check if there is any corner empty. If empty, then we place letter in that position
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    # randomly select a corner to move into
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    # Place letter at center position
    if 5 in possibleMoves:
        move = 5
        return move

    # Check if there is any edge empty, if empty, place the letter in that edge position
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
            # randomly select a corner to move into
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move


def selectRandom(li):
    return random.choice(li)


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

# User = X
# Bot = O


def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not (isBoardFull(board)):
        if not isWinner(board, 'O'):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this game!')
            break

        if not isWinner(board, 'X'):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('X\'s won this game, good job!')
            break

    if isBoardFull(board):
        print('Game Over')


main()

while True:
    print()
    answer = input("Do you want to play again? (Y|N): ")
    print()
    if answer.lower() == 'y':
        board = [' ' for i in range(10)]
        main()
    else:
        break

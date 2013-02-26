# Tic Tac Toe
import random
def drawGameBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3],)
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
def makeMove(board, letter, move):
    board[move] = letter
def isWinner(board, letter):

    return ((board[1] == letter and board[2] == letter and board[3] == letter) or # across the top
            (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
            (board[7] == letter and board[8] == letter and board[9] == letter) or # across the bottom
            (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
            (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
            (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
            (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
            (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal
def getGameBoardCopy(board):
    dupeGameBoard = []
    for i in board:
        dupeGameBoard.append(i)
    return dupeGameBoard
def isSpaceFree(board, move):
    return board[move] == ' '
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
        # First, check if computer can win in next move.
    for i in range(1, 10):
        copy = getGameBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
                # Second, check if computer can block a winning move.
    for i in range(1, 10):
        copy = getGameBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
                # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5
        # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
        # Move on one of the sides if nothing else
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
def isGameBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
print('Welcome to Meagan\'s Unbeatable Tic Tac Toe!')
while True:
    theGameBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            drawGameBoard(theGameBoard)
            move = getPlayerMove(theGameBoard)
            makeMove(theGameBoard, playerLetter, move)
            if isWinner(theGameBoard, playerLetter):
                drawGameBoard(theGameBoard)
                print('You win.')
                gameIsPlaying = False
            else:
                if isGameBoardFull(theGameBoard):
                    drawGameBoard(theGameBoard)
                    print('The game is a tie.')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theGameBoard, computerLetter)
            makeMove(theGameBoard, computerLetter, move)
            if isWinner(theGameBoard, computerLetter):
                drawGameBoard(theGameBoard)
                print('You Lose.')
                gameIsPlaying = False
            else:
                if isGameBoardFull(theGameBoard):
                    drawGameBoard(theGameBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break

# Tic Tac Toe
import random
def instructions():
    print("""
You will make your move by entering a number, 1 - 9.
The number will correspond to the board position as shown below

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

Have fun, and good luck.

"""
    )
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
# All Moves
            # Winning Top Row
    if (board[1] == computerLetter and board[2] == computerLetter) and isSpaceFree(board,3):
        return 3;
    if (board[1] == computerLetter and board[3] == computerLetter) and isSpaceFree(board,2):
        return 2;
    if (board[2] == computerLetter and board[3] == computerLetter) and isSpaceFree(board,1):
        return 1;

            # Winning Second Row
    if (board[4] == computerLetter and board[5] == computerLetter) and isSpaceFree(board,6):
        return 6;
    if (board[4] == computerLetter and board[6] == computerLetter) and isSpaceFree(board,5):
        return 5;
    if (board[5] == computerLetter and board[6] == computerLetter) and isSpaceFree(board,4):
        return 4;

        # Winning Third Row
    if (board[7] == computerLetter and board[8] == computerLetter) and isSpaceFree(board,9):
        return 9;
    if (board[7] == computerLetter and board[9] == computerLetter) and isSpaceFree(board,8):
        return 8;
    if (board[8] == computerLetter and board[9] == computerLetter) and isSpaceFree(board,7):
        return 7;

        # Winning First Column

    if (board[1] == computerLetter and board[4] == computerLetter) and isSpaceFree(board,7):
        return 7;
    if (board[1] == computerLetter and board[7] == computerLetter) and isSpaceFree(board,4):
        return 4;
    if (board[4] == computerLetter and board[7] == computerLetter) and isSpaceFree(board,1):
        return 1;

        # Winning Second Column
    if (board[2] == computerLetter and board[5] == computerLetter) and isSpaceFree(board,8):
        return 8;
    if (board[2] == computerLetter and board[8] == computerLetter) and isSpaceFree(board,5):
        return 5;
    if (board[5] == computerLetter and board[8] == computerLetter) and isSpaceFree(board,2):
        return 2;

        # Winning Third Column
    if (board[3] == computerLetter and board[6] == computerLetter) and isSpaceFree(board,9):
        return 9;
    if (board[3] == computerLetter and board[9] == computerLetter) and isSpaceFree(board,6):
        return 6;
    if (board[6] == computerLetter and board[9] == computerLetter) and isSpaceFree(board,3):
        return 4;

        # Winning Left to Right Diagonal
    if (board[1] == computerLetter and board[5] == computerLetter) and isSpaceFree(board,9):
        return 9;
    if (board[1] == computerLetter and board[9] == computerLetter) and isSpaceFree(board,5):
        return 5;
    if (board[5] == computerLetter and board[9] == computerLetter) and isSpaceFree(board,1):
        return 1;

        # Winning Right to Left Diagonal
    if (board[3] == computerLetter and board[5] == computerLetter) and isSpaceFree(board,7):
        return 7;
    if (board[3] == computerLetter and board[7] == computerLetter) and isSpaceFree(board,5):
        return 5;
    if (board[5] == computerLetter and board[7] == computerLetter) and isSpaceFree(board,3):
        return 3;

            # Top Row Horizontal Blocking
    if (board[1] == playerLetter and board[2] == playerLetter) and isSpaceFree(board,3):
        return 3;
    if (board[2] == playerLetter and board[3] == playerLetter) and isSpaceFree(board,1):
        return 1;
    if (board[1] == playerLetter and board[3] == playerLetter) and isSpaceFree(board,2):
        return 2;

            # Second Row Horizontal Blocking
    if (board[4] == playerLetter and board[5] == playerLetter) and isSpaceFree(board,6):
        return 6;
    if (board[5] == playerLetter and board[6] == playerLetter) and isSpaceFree(board,4):
        return 4;
    if (board[4] == playerLetter and board[6] == playerLetter) and isSpaceFree(board,5):
        return 5;

            # Third Row Horizontal Blocking
    if (board[7] == playerLetter and board[8] == playerLetter) and isSpaceFree(board,9):
        return 9;
    if (board[8] == playerLetter and board[9] == playerLetter) and isSpaceFree(board,7):
        return 7;
    if (board[7] == playerLetter and board[9] == playerLetter) and isSpaceFree(board,8):
        return 8;

            # First Column Vertical Blocking
    if (board[1] == playerLetter and board[4] == playerLetter) and isSpaceFree(board,7):
        return 7;
    if (board[4] == playerLetter and board[7] == playerLetter) and isSpaceFree(board,1):
        return 1;
    if (board[1] == playerLetter and board[7] == playerLetter) and isSpaceFree(board,4):
        return 4;

            # Second Column Vertical Blocking
    if (board[2] == playerLetter and board[5] == playerLetter) and isSpaceFree(board,8):
        return 8;
    if (board[5] == playerLetter and board[8] == playerLetter) and isSpaceFree(board,2):
        return 2;
    if (board[2] == playerLetter and board[8] == playerLetter) and isSpaceFree(board,5):
        return 5;

            # Third Column Vertical Blocking
    if (board[3] == playerLetter and board[6] == playerLetter) and isSpaceFree(board,9):
        return 9;
    if (board[3] == playerLetter and board[9] == playerLetter) and isSpaceFree(board,6):
        return 6;
    if (board[6] == playerLetter and board[9] == playerLetter) and isSpaceFree(board,3):
        return 3;

            # Left to Right Diagonal
    if(board[1] == playerLetter and board[5] == playerLetter) and isSpaceFree(board,9):
        return 9;
    if(board[1] == playerLetter and board[9] == playerLetter) and isSpaceFree(board,5):
        return 5;
    if(board[5] == playerLetter and board[9] == playerLetter) and isSpaceFree(board,1):
        return 1;

            # Right to Left Diagonal
    if (board[3] == playerLetter and board[5] == playerLetter) and isSpaceFree(board,7):
        return 7;
    if (board[3] == playerLetter and board[7] == playerLetter) and isSpaceFree(board,5):
        return 5;
    if (board[5] == playerLetter and board[7] == playerLetter) and isSpaceFree(board,3):
        return 3;

        # Take Center if it's Free
    if isSpaceFree(board, 5):
        return 5

        # Counteract if they form a diagonal with PL in 5 and in 9
    if (board[5] == playerLetter and board[1] == computerLetter and board[9] == playerLetter) and isSpaceFree(board,6):
        return 6;
    if (board[5] == playerLetter and board[1] == computerLetter and board[9] == playerLetter) and isSpaceFree(board,8):
        return 8;
    if (board[5] == playerLetter and board[1] == computerLetter and board[9] == playerLetter) and isSpaceFree(board,7):
        return 7;
    if (board[5] == playerLetter and board[1] == computerLetter and board[9] == playerLetter) and isSpaceFree(board,3):
        return 3;

        # Counteract if they form a diagonal with PL in 5 and in 1
    if (board[5] == playerLetter and board[9] == computerLetter and board[1] == playerLetter) and isSpaceFree(board,2):
        return 2;
    if (board[5] == playerLetter and board[9] == computerLetter and board[1] == playerLetter) and isSpaceFree(board,4):
        return 4;
    if (board[5] == playerLetter and board[9] == computerLetter and board[1] == playerLetter) and isSpaceFree(board,7):
        return 7;
    if (board[5] == playerLetter and board[9] == computerLetter and board[1] == playerLetter) and isSpaceFree(board,3):
        return 3;

        # Counteract if they form a diagonal with PL in 5 and in 7
    if (board[5] == playerLetter and board[3] == computerLetter and board[7] == playerLetter) and isSpaceFree(board,1):
        return 1;
    if (board[5] == playerLetter and board[3] == computerLetter and board[7] == playerLetter) and isSpaceFree(board,9):
        return 9;
    if (board[5] == playerLetter and board[3] == computerLetter and board[7] == playerLetter) and isSpaceFree(board,4):
        return 4;
    if (board[5] == playerLetter and board[3] == computerLetter and board[7] == playerLetter) and isSpaceFree(board,8):
        return 8;

        # Counteract if a diagonal with CL in 5 and PL in 1 & 9
    if (board[1] == playerLetter and board[5] == computerLetter and board[9] == playerLetter) and isSpaceFree(board,2):
        return 2;
    if (board[1] == playerLetter and board[5] == computerLetter and board[9] == playerLetter) and isSpaceFree(board,8):
        return 8;


        # Counteract if diagonal with CL in 5 and PL in 3 & 7
    if (board[3] == playerLetter and board[5] == computerLetter and board[7] == playerLetter) and isSpaceFree(board,2):
        return 2;
    if (board[3] == playerLetter and board[5] == computerLetter and board[7] == playerLetter) and isSpaceFree(board,8):
        return 8;



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
instructions()
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

import random

def TicTacToe():
    '''
    This is a game of tic tac toe that can be played in a terminal. To play just call this function and then follow
    the directions provided throughout the game. You will be playing against a CPU that choses random spots
    still available on the board.
    '''
    displayArr = [1,2,3,4,5,6,7,8,9]
    spacesLeft = [1,2,3,4,5,6,7,8,9]
    enderText = checkWinner(displayArr)
    startup = input("Welcome to Tic Tac Toe, to begin press enter!")
    while enderText == "No Winner":
        createScreen(displayArr)
        pickedSpot = requestInput(spacesLeft)
        displayArr[pickedSpot-1] = 'X'
        enderText = checkWinner(displayArr)
        if len(spacesLeft) > 0:
            CPUPickedSpot = cpuPlayer(spacesLeft)
            displayArr[CPUPickedSpot-1] = 'O'
        else:
            enderText = "Cats Game"
            break
        enderText = checkWinner(displayArr)
        
    createScreen(displayArr)
    if enderText == "X Wins":
        print("WINNER WINNER WINNER!!!!!")
        tryAgain()
    elif enderText == "O Wins":
        print("You Lost:(")
        tryAgain()
    else:
        print("It's a Tie!")
        tryAgain()
        
def tryAgain():
    '''
    This simply asks the user if they want to play again. If the user replys with a 'y' then the game will run again
    '''
    tryagain = input("Would you like to try again [y/n]: ")
    if tryagain.lower() == "y":
        TicTacToe()
def cpuPlayer(availablePositions):
    '''
    this takes in a list of the positions still available on the board and then randomly chooses one of these spots
    and returns it acting as a CPU.
    '''
    picked = random.choice(availablePositions)
    availablePositions.remove(picked)
    return picked

def checkWinner(displayArr):
    '''
    This takes a list as an input and checks to see if any of the patterns on the board is a winning pattern and
    returns a string to correspond to if there is a winner and who it is.
    '''
    counter = 0
    chunked = [displayArr[i * 3:(i + 1) * 3] for i in range((len(displayArr) + 3 - 1) // 3 )]
    for row in chunked:
        if len(set(row)) == 1:
            return f"{row[0]} Wins"
    for item in chunked[0]:
        if item == chunked[1][counter] and item == chunked[2][counter]:
            return f"{item} Wins"
        counter += 1
    if displayArr[0] == displayArr[4] and displayArr[0] == displayArr[8]:
        return f"{displayArr[0]} Wins"
    elif displayArr[2] == displayArr[4] and displayArr[2] == displayArr[6]:
        return f"{displayArr[2]} Wins"
    
    return "No Winner"


def requestInput(availablePositions = range(1,10)):
    '''
    This takes the input of an array. It then asks the player to provide a position they want to place their 'x'
    and it returns this position
    '''
    posAvail = False
    userInput = ""
    
    while userInput.isdigit() == False or posAvail == False:
        
        posAvail = False
        userInput = input("Chose a diget above to replace with X: ")
        
        if userInput.isdigit():
            if int(userInput) in availablePositions:
                posAvail = True
            else:
                print("That space is not available!")
        else:
            print("Enter a valid space number to replace!")
    availablePositions.remove(int(userInput))        
    return int(userInput)

def createScreen(positionArr = range(1,10)):
    '''
    This displays the tic tac toe screen and takes in an array of 9 digets for each of the positions on the screen.
    each item in this list correspond to a place on the tic tac toe board.
    '''
    if len(positionArr) != 9:
        positionArr = range(1,10)
    print(f" {str(positionArr[0])}|{str(positionArr[1])}|{str(positionArr[2])}")
    print(f"-------")
    print(f" {str(positionArr[3])}|{str(positionArr[4])}|{str(positionArr[5])}")
    print(f"-------")
    print(f" {str(positionArr[6])}|{str(positionArr[7])}|{str(positionArr[8])}")

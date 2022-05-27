import random

numberOfGuesses = 1     # initalize our number of guesses variable
userGuess = -1          # initialize our guess variable

# we try to turn the input into an int, if it doesn't work, send another input request with a note to only use ints
def userGuessToInt():
    try:
        global userGuess
        userGuess = int(userGuess)
    except:
        getInput("notInt")



def checkAnswer():
    global numberOfGuesses
    numberOfGuesses = numberOfGuesses + 1 # each cycle add 1 to the numberOfGuesses variable

    if (isinstance(userGuess, int)):
        # this doesn't check if the number is equal to the number to guess, because it will never make it to checkAnswer() if the number has been guessed (see the while statement that leads to checkAnswer())
        if (userGuess < numberToGuess):
            getInput("tooLow")
        elif (userGuess > numberToGuess):
            getInput("tooHigh")
        else:
            print("An error has occurred, please restart the program\n")
    else:
        #print("User guess is of type: " + str(type(userGuess)))
        getInput("notInt")



def getInput(inputType):

    global userGuess

    if (inputType == "initial"):
        # request a guess from the user
        print('I have selected a whole number between ' + str(lowBoundary) + ' and ' + str(highBoundary) + '..')
        userGuess = input("Go ahead, give me a guess: \n")
    elif (inputType == "notInt"):
        # request a whole number
        userGuess = input("Please, only give me a whole number between " + str(lowBoundary) + "and" + str(highBoundary) + "\n")
    elif (inputType == "tooHigh"):
        # give high feedback and get another input
        userGuess = input("Too High! Guess again\n")
    elif (inputType == "tooLow"):
        # give low feedback and get another input
        userGuess = input("Too Low, guess again!\n")
    else:
        print("An error has occurred, please restart the program\n")

    # attempt to change the user's guess to an int, if not, send a "notInt" input request
    userGuessToInt()





######-----* Start of code *-----###### (non-function)
lowBoundary = 1
highBoundary = 100

# select a random number with the boundaries above
numberToGuess = random.randint(lowBoundary,highBoundary)

getInput("initial")     # get input via the getInput function

# continue looping, as long as the user hasn't guessed the number
while (userGuess != numberToGuess):
    checkAnswer()
else:       # as soon as the user has guessed it, run the following (i.e. userGuess == numberToGuess)
    print("You've WON!!! Congratulations!\n\nNumber of Guesses: " + str(numberOfGuesses))

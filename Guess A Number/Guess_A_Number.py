import random
import sys

lowLimit = 1
highLimit = 10
previousNumbers = []

def choose():
    global previousNumbers
    previousNumbers = []

    print("I've picked a number from " + str(lowLimit) + " to " + str(highLimit) + ".")
    global target
    target = random.randint(lowLimit, highLimit)

    #Print target number for debug#
    #print("Target: " + str(target))

def promptGuess():
    try:
        global previousNumbers
        global guess

        print
        if len(previousNumbers) > 0:
            print ("Previous tries: " + str(previousNumbers).strip("[]"))

        guess = input("What's your guess? ")
        if guess < lowLimit:
            print
            print("Guess is too low. Try again please.")
            promptGuess()
        elif guess > highLimit:
            print
            print("Guess is too high. Try again please.")
            promptGuess()
        else:
            previousNumbers.append(guess)
            test(guess)
    except (NameError, SyntaxError):
        print
        print("Oops. Please choose a number from " + str(lowLimit) + " to " + str(highLimit) + ".")
        promptGuess()

def test(x):
    global diff
    diff = target - x

    #Print difference for debugging
    #print("Difference: " + str(diff))

    if diff == 0:
        print
        print("You got it, yay!")
        print("Press 'y' to play again. Press 'n' to quit.")
        x = str(raw_input())
        if x == "y":
            choose()
            promptGuess()

        elif x == "n":
            sys.exit()

        else:
            print
            print("Please choose 'y' or 'n'.")

    elif diff <= -4:
        print
        print("Sorry, way too high. Try again.")
        promptGuess()

    elif diff >= 4:
        print
        print("Sorry, way too low. Try again.")
        promptGuess()

    elif diff < 0 and diff > -4:
        print
        print("So close! Just a little bit high. Keep guessing.")
        promptGuess()

    elif diff > 0 and diff < 4:
        print
        print("So close! Just a little bit low. Keep guessing.")
        promptGuess()


choose()
promptGuess()


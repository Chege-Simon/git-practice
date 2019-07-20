import random

secretNumber = random.randint(1,20)

global numberOfGuesses
numberOfGuesses = 0

def game(secretNumber):
    print("Am thinking of a number between 1 and 20.")
    print("Take a guess.")
    guessLimit = 6
    #global numberOfGuesses
    
    while numberOfGuesses <= guessLimit:
        
        yourNumber = int(input())
        
        numberOfGuesses = numberOfGuesses + 1
        
        if yourNumber < secretNumber:
            print("your guess is to low.")
        elif yourNumber > secretNumber:
            print("Your guess is too high.")
        else:
            break
    if yourNumber == secretNumber:
        print("Good job! You guessed my number in " +
                  str(numberOfGuesses) + " guesses !")
    else:
        print('Nope. The number I was thinking of was '
             + str(secretNumber))

game(secretNumber)
        

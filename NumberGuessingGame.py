from random import randint
from goto import with_goto


# checks for the user selected level and calls the required level function
def play(level):

    #in case of an input error, the program catches it and goes back to ask for the proper input value
    try:
        if level=='easy':
            print("Guess a number between 1-10")
            easy() #calling the easy level function
        elif level == 'medium':
            print("Guess a number between 1-20")
            medium() #calling the medium level function
        elif level == 'hard':
            print("Guess a number between 1-50")
            hard()#calling the hard level function

    except ValueError:
        print("Invalid Level! \n Please enter a valid level!!")
        goto .enterLevel #once an error is catched, it redirects to line 82


#this function deals with accepting the player's guess and ensuring it is an integer
@with_goto
def userGuess():
    label .guess
    try:
        guess = int(input("Guess: "))
        return guess
    except ValueError:
        print("Invalid Input. \n Please enter an integer value.")
        goto .guess # once a value error is encountered, it goes back to ask for a correct input instead
        #the program


# this function generates a random number and checks if the player's guess corresponds
#it accepts two parameters : number of guesses and generated random number.
# as these two parameters varies according to level
def guessChecker(a, b):

    guessCount = 0
    while guessCount < a:
        guess = userGuess()
        guessCount += 1

        if guess == b :
            print("You got it right!")
            break
        else:
            leftguesses = a-guessCount
            print("That was wrong!")
            print( "You have", leftguesses, "guesses left!")
    else:
        print("Game Over!")


# easy level function
def easy():

    number_of_guesses = 6
    rand = randint(1,10)

    guessChecker(number_of_guesses, rand) #Calling the guess checker


#medium level function
def medium():
    number_of_guesses = 4
    rand = randint(1, 20)

    guessChecker(number_of_guesses, rand) #Calling the guess checker


#hard level function
def hard():
    number_of_guesses = 3
    rand = randint(1, 50)

    guessChecker(number_of_guesses, rand)


#the main function
@with_goto
def main():

    label .enterLevel
    selectLevel = input("Select game level. \n Easy \t Medium \t Hard\n ").lower()
    play(selectLevel)

    tryAgain = input("Do you want to try again?(y/n) : ")#giving the player a chance to end the game himself

    if tryAgain == "y":
        goto .enterLevel
    else:
        exit()


main() #calling the main funtion
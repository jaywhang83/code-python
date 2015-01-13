__author__ = 'student'
import random # Imports random function so it can be used

game_init = raw_input("Would you like to play a guessing game? ")
random_number = random.randrange(100) # Generate random number range up to 100


def start_game():
    limit = 5 # Sets limit to how many guesses player can get
    tries = 0 # Hold/counts amount of players guesses
    while tries != limit:
        user_input = int(raw_input("I'm thinking of a number between 1 to 100.\nGuess what it is: "))
        tries += 1 # Increments players guess by one
        if tries == limit: # Players guess equals limit then exits program
            print "you are out of tries"
            exit()
        if user_input == random_number:
            """
            If player guess right , displays message that player guess the number right.
            Also prints string value of random_number. Then exit the program
            """
            print "Good job! You got it right! it was " + str(random_number)
            exit()
            """
            If player guess is greater than random_number,
            Prints the message telling player that number is too high
            Also prints string value of random_number.
            """
        elif user_input > random_number:
            print "You guessed wrong. " + str(user_input) + " is too high. Guess again."
            """
            If player guess is less than random_number,
            Prints the message telling player that number is too low
            Also prints string value of random_number.
            """
        elif user_input < random_number:
            print "You guessed wrong. " + str(user_input) + " is too low. Guess again."

if game_init == "yes": # Executes the start_game function
    start_game()

else: # prints the message then exits the game
    print "You are no fun. Goodbye!"
    exit()

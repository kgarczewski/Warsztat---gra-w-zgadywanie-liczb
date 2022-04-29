from random import randint


def get_the_number():

    hidden_number = randint(1, 101)
    print("I am thinking of a number between 1 and 100. Can You guess it?")
    while True:

        """Get number from user"""
        try:
            user_guess = (input('Guess a number! '))
            user_guess = int(user_guess)
            if not 100>user_guess>0:
                print("It is not in between 1 and 101!")

        except ValueError:
            print("Its not a number!")
            continue
        if user_guess == hidden_number and user_guess in range(1, 101):
            print("You win!")
            break
        if user_guess > hidden_number and user_guess in range(1, 101):
            print("Too big!")
        if user_guess < hidden_number and user_guess in range(0, 101):
            print("Too small!")

get_the_number()
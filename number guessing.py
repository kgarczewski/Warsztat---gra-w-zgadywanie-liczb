from random import randint


def get_the_number():
    """Get number from user"""
    while True:
        user_guess = (input("Guess the number: "))
        try:
            result = int(user_guess)
            break

        except ValueError:
            print("It's not a number!")

    return result


def guess_the_number():

    """Main game function."""

    hidden_number = randint(1, 100)
    user_number = get_the_number()
    while user_number != hidden_number:
        if user_number < hidden_number:
            print("Too small!")
        else:
            print("Too big!")
        user_number = get_the_number()
    print("You Win!")


guess_the_number()

"""
* A Guessing Game in Python
* @author Michael Le
* @youtube michaelworkspace
* @version python 3.7.3
"""

from random import randint

correct_number = randint(0, 100)
max_guesses = 5


def begin_game():

    guess_limit = 5
    game_running = True

    while game_running:
        try:
            guess = int(input("Guess a number from 1 to 100\n"))
        except ValueError:
            print(
                "Dude... that's not a number. Please guess a number from 1 to 100")
            continue
        if guess == correct_number:
            print("You've got it! Good Job")
            game_running = False
        else:
            guess_limit -= 1
            print(f"WRONG! Guess again. You have {guess_limit} left")
            if guess < correct_number:
                print("Hint: Guess higher\n")
            else:
                print("Hint: Guess lower\n")
            if (guess_limit is 0):
                print("You are out of guesses. Game over")
                game_running = False


if __name__ == '__main__':
    begin_game()

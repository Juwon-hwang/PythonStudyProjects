import logo
import random
import os

easy = 10
hard = 5

def set_number():
    """ Computer choose random number """
    return random.randint(1, 100)

def set_level(level):
    """ User choose the level"""
    if level == "easy":
        print("You have 10 attempts")
        return easy
    elif level == "hard":
        print("You have 5 attempts")
        return hard
    else:
        print("Enter easy and hard correctly")
        return set_level(input("Choose a difficulty, Type 'easy' or 'hard': "))

def compare(user_number, computer_number):
    """Compare the user Number is right"""
    if user_number == computer_number:
        print("Win")
        return True
    elif user_number > computer_number:
        print("Too high")
    elif user_number < computer_number:
        print("Too low")
    return False

def attempt_count_down(attempts):
    attempts -= 1
    if attempts == 0:
        print("You have no attempts left.")
        print("You lose")
        return 0
    else:
        print(f"You have {attempts} attempts remaining.")
        return attempts

def startGame():
    print(logo)
    computer_number = set_number()
    print("I'm thinking of number between 1 and 100")
    level = input("Choose a difficulty, Type 'easy' or 'hard': ")
    attempts = set_level(level)

    game_over = False
    while attempts > 0 and not game_over:
        user_number = int(input("Make a guess: "))
        if compare(user_number, computer_number):
            game_over = True
        else:
            attempts = attempt_count_down(attempts)
            if attempts == 0:
                game_over = True

    play_again = input("Do you want to play again? Type 'yes' or 'no': ")
    if play_again == 'yes':
        os.system("cls" if os.name == "nt" else "clear")  # 'cls' for Windows, 'clear' for Unix
        startGame()
    else:
        print("Thanks for playing! Goodbye.")

startGame()
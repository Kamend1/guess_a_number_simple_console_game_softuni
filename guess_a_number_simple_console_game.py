import random
from math import inf

min_number = 1
max_number = 100
number_attempts = 0
best_score = inf

computer_number = random.randint(min_number, max_number)
player_name = input("Please enter your name: ")

while True:

    try:
        player_input = int(input(f"Guess a number from {min_number} to {max_number}: "))
    except ValueError:
        print("Invalid number. Please try again...")
        continue

    number_attempts += 1
    if player_input < min_number or player_input > max_number:
        print("Invalid number. Please try again...")
        continue

    if player_input > computer_number:
        print("Too high")
        continue
    elif player_input < computer_number:
        print("Too low")
        continue
    elif player_input == computer_number:
        if number_attempts < best_score:
            best_score = number_attempts
        print("You guessed it!")
        print(f"{player_name}, you guessed {computer_number} in {number_attempts} attempts.", end=" ")
        print(f"Your best score for this game is {best_score} attempts")
    number_attempts = 0

    restart = input("Type [yes] if you would like to play again and [no] to exit: ")
    while restart not in ['yes', 'no']:
        print("Invalid Input. Try again...")
        restart = input("Type [yes] if you would like to play again and [no] to exit: ")
    if restart == "no":
        print("Thank you for playing!")
        break
    else:
        computer_number = random.randint(min_number, max_number)

    restart = ""

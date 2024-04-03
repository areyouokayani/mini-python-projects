#  A simple python script to roll a dice.
#  It takes in a user input to determine the number of sides the dice has

import random

while True:

    try:
        x = int(input("How many sides does your dice have?: "))
    except ValueError:
        print("Please enter a valid number i.e. 6")
        continue

    if x < 2:
        print("A dice must have at least 2 sides!")
        continue

    num = random.randint(1, x)
    print(f"You rolled a {num}" )

    while True:

        a = input("Would you like to roll again? y or n: ").lower()

        if a == "n":
          break

        elif a == "y":
            break

        else:
            print("Please enter y or n")

    if a == "n":
        break
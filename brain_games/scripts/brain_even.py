#!/usr/bin/env python

import prompt
from random import randint
from brain_games.scripts.brain_games import main as greeting


def game():
    name = greeting()
    point_counter = 0
    print(f"{name} Answer 'yes' if the number is even, otherwise answer 'no'.")
    while (point_counter < 3):
        x = randint(1, 100)
        print(f"Question: {x}")
        answer = prompt.string("Your answer: ")
        if (answer == "yes") and (x % 2 == 0):
            point_counter += 1
            print("Correct!")
        elif (answer == "no") and (x % 2 != 0):
            point_counter += 1
            print(f"Correct{name}!")
        else:
            print(f"Nooo {name} You loose! :(")
            return
    if point_counter < 2:
        return
    print(f"Congratulations, {name} You WIN")

def main():
    game()


if __name__ == '__main__':
    main()

#!/usr/bin/env python

import prompt
from math import gcd
from random import randint
from brain_games.scripts.brain_games import main as greeting


def game():
    name = greeting()
    point_counter = 0
    print("Find the greatest common divisor of given numbers.")
    while (point_counter < 3):
        x = randint(0, 99)
        y = randint(0, 99)
        need = str(gcd(x, y))
        print(f"Question: {x} {y}")
        answer = prompt.string("Your answer: ")
        if answer == need:
            point_counter += 1
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was"
                f"'{need}'. Let's try again, {name}!"
                )
            return
    if point_counter < 2:
        return
    print(f"Congratulations, {name}!")


def main():
    game()


if __name__ == '__main__':
    main()

#!/usr/bin/env python

import prompt
from math import sqrt
from random import randint
from brain_games.scripts.brain_games import main as greeting


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


def game():
    name = greeting()
    point_counter = 0
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    while (point_counter < 3):
        number = randint(0, 99)
        need = is_prime(number)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        if (answer == "yes") and (need is True):
            point_counter += 1
            print("Correct!")
        elif (answer == "no") and (need is False):
            point_counter += 1
            print("Correct!")
        else:
            need = "yes" if need is True else 'no'
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was"
                f" '{need}'. Let's try again, {name}!"
            )
            return
    if point_counter < 2:
        return
    print(f"Congratulations, {name}!")


def main():
    game()


if __name__ == '__main__':
    main()

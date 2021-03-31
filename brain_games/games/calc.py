#!/usr/bin/env python

import prompt
from operator import add, sub, mul
from random import randint, choice
from brain_games.scripts.brain_games import main as greeting


def game():
    operators = {'+': add, '-': sub, '*': mul, }
    name = greeting()
    point_counter = 0
    print("What is the result of the expression?")
    while (point_counter < 3):
        x = randint(0, 99)
        y = randint(0, 99)
        operator = choice(['+', '-', '*', ])
        need = str(operators[operator](x, y))
        print(f"Question: {x} {operator} {y}")
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

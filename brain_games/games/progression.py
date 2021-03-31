#!/usr/bin/env python

import prompt
from random import randint
from brain_games.scripts.brain_games import main as greeting


def game():
    name = greeting()
    point_counter = 0
    print("What number is missin in the progression?")
    while (point_counter < 3):
        progression_len = randint(5, 10)
        progression_step = randint(1, 12)
        progression_start = randint(0, 99)
        random_pick = randint(0, progression_len)
        progression = [str(i) for i in range(progression_start,
                                             progression_step
                                             * progression_len
                                             + progression_start,
                                             progression_step)]
        need = progression[random_pick]
        progression[random_pick] = '..'
        print(f"Question: {' '.join(progression)}")
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

#!/usr/bin/env python3
from brain_games.games.calc import run_calc
from brain_games.engine import run

RULE = 'What is the result of the expression?.'


def main():
    run(run_calc, RULE)


if __name__ == '__main__':
    main()

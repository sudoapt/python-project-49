#!/usr/bin/env python3
from brain_games.games.calc_game import calc_game
from brain_games.engine import run

RULE_ = 'What is the result of the expression?.'


def main():
    run(calc_game, RULE_)

if __name__ == '__main__':
    main()
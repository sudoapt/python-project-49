#!/usr/bin/env python3
from brain_games.games.even_game import even_game
from brain_games.engine import run

RULE_ = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run(even_game, RULE_)


if __name__ == '__main__':
    main()

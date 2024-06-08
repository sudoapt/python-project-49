#!/usr/bin/env python3
from brain_games.games.gcd_game import gcd_game
from brain_games.engine import run

RULE_ = "Find the greatest common divisor of given numbers."


def main():
    run(gcd_game, RULE_)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
from brain_games.games.progression_game import progression_game
from brain_games.engine import run

RULE_ = "What number is missing in the progression?"


def main():
    run(progression_game, RULE_)


if __name__ == '__main__':
    main()

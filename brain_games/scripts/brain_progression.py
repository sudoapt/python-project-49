#!/usr/bin/env python3
from brain_games.games.progression import run_progression
from brain_games.engine import run

RULE = "What number is missing in the progression?"


def main():
    run(run_progression, RULE)


if __name__ == '__main__':
    main()

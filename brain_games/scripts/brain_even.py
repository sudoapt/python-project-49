#!/usr/bin/env python3
from brain_games.games.even import run_even
from brain_games.engine import run

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run(run_even, RULE)


if __name__ == '__main__':
    main()

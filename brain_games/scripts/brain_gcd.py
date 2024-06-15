#!/usr/bin/env python3
from brain_games.games.gcd import run_gcd
from brain_games.engine import run

RULE = "Find the greatest common divisor of given numbers."


def main():
    run(run_gcd, RULE)


if __name__ == '__main__':
    main()

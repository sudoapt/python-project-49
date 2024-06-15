#!/usr/bin/env python3
from brain_games.games.prime import run_prime
from brain_games.engine import run

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run(run_prime, RULE)


if __name__ == '__main__':
    main()

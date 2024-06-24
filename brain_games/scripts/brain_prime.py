#!/usr/bin/env python3
from brain_games.games.prime import get_prime
from brain_games.engine import run


def main():
    run(get_prime)


if __name__ == '__main__':
    main()

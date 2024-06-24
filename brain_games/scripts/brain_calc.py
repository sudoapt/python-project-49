#!/usr/bin/env python3
from brain_games.games.calc import get_calc
from brain_games.engine import run


def main():
    run(get_calc)


if __name__ == '__main__':
    main()

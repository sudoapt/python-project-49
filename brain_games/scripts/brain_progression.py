#!/usr/bin/env python3
from brain_games.games.progression import get_progression
from brain_games.engine import run


def main():
    run(get_progression)


if __name__ == '__main__':
    main()

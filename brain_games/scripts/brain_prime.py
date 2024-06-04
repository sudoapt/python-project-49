#!/usr/bin/env python3
from brain_games.games.prime_game import prime_game
from brain_games.engine import run

RULE_ = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run(prime_game, RULE_)


if __name__ == '__main__':
    main()
    

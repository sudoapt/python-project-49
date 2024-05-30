import random

MIN_NUM = 1
MAX_NUM = 100


def even_game():
    rand_int = random.randint(MIN_NUM, MAX_NUM)
    answer = 'yes' if rand_int % 2 == 0 else 'no'
    return rand_int, answer
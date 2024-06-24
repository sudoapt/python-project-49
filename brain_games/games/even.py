import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def get_even():
    print(RULE)
    rand_int = random.randint(MIN_NUM, MAX_NUM)
    answer = 'yes' if rand_int % 2 == 0 else 'no'
    return rand_int, answer

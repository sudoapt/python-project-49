import random
import math

MIN_NUM = 2
MAX_NUM = 10


def run_prime():
    rand_int = random.randint(MIN_NUM, MAX_NUM)
    is_prime = True
    for i in range(2, math.isqrt(rand_int) + 1):
        if rand_int % i == 0:
            is_prime = False
            break

    answer = 'yes' if is_prime else 'no'
    return rand_int, answer

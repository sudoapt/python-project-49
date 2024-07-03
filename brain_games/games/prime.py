import random
import math


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    is_prime = True
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            is_prime = False
            break
    return is_prime


def get_question_and_answer():
    rand_int = random.randint(2, 10)
    question = is_prime(rand_int)
    answer = 'yes' if question else 'no'
    return rand_int, answer

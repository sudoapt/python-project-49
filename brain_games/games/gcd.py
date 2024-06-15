import random
import math

MIN_NUM = 1
MAX_NUM = 100


def run_gcd():
    arg1 = random.randint(MIN_NUM, MAX_NUM)
    arg2 = random.randint(MIN_NUM, MAX_NUM)
    question = f"{arg1} {arg2}"
    result = str(math.gcd(arg1, arg2))

    return question, result

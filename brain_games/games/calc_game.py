import random

MIN_NUM = 1
MAX_NUM = 10


def calc_game():
    arg1 = random.randint(MIN_NUM, MAX_NUM)
    arg2 = random.randint(MIN_NUM, MAX_NUM)
    operations = random.choice(['+', '-', '*'])

    if operations == '+':
        result = arg1 + arg2
    elif operations == '-':
        result = arg1 - arg2
    elif operations == '*':
        result = arg1 * arg2

    result_str = str(result)
    math = f"{arg1} {operations} {arg2}"
    return math, result_str

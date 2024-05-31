import random

MIN_NUM = 1
MAX_NUM = 10


def calc_game():
    arg1 = random.randint(MIN_NUM, MAX_NUM)
    arg2 = random.randint(MIN_NUM, MAX_NUM) 
    operations = random.choice(['+', '-', '*'])
    math = f"{arg1} {operations} {arg2}"
    result = str(eval(math))
    return math, result
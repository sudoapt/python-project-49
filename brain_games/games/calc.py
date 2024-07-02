import random

RULE = 'What is the result of the expression?'
MIN_NUM = 1
MAX_NUM = 10


def get_question_and_answer():
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

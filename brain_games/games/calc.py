import random
from operator import add, sub, mul

RULE = 'What is the result of the expression?'


def get_question_and_answer():
    arg1 = random.randint(1, 10)
    arg2 = random.randint(1, 10)

    operators = ((add, "+"), (sub, "-"), (mul, "*"))
    operation = random.choice(operators)
    operator, str_operator = operation[0], operation[1]

    result_str = str(operator(arg1, arg2))
    math = f"{arg1} {str_operator} {arg2}"
    return math, result_str

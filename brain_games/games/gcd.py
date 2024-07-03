import random
import math

RULE = "Find the greatest common divisor of given numbers."


def get_question_and_answer():
    arg1 = random.randint(1, 100)
    arg2 = random.randint(1, 100)
    question = f"{arg1} {arg2}"
    result = str(math.gcd(arg1, arg2))

    return question, result

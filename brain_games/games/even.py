import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    rand_int = random.randint(1, 100)
    answer = 'yes' if rand_int % 2 == 0 else 'no'
    return rand_int, answer

import random

RULE = "What number is missing in the progression?"


def make_progression():
    progression = list(range(1, 100, random.randint(1, 5)))
    rand_index = random.randint(0, len(progression) - 5)
    return progression[rand_index:rand_index + random.randint(5, 10)]


def get_question_and_answer():
    progression = make_progression()
    rand_index = random.randint(0, len(progression) - 1)
    answer = progression[rand_index]
    progression[rand_index] = '..'
    return ' '.join(map(str, progression)), str(answer)

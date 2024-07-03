import random

RULE = "What number is missing in the progression?"
MAX_LENTH = 10
MIN_LENTH = 5
MAX_STEP = 5
MIN_STEP = 1
MAX_NUMBER = 100
MIN_NUMBER = 1


def make_progression():
    progression = list(range(MIN_NUMBER, MAX_NUMBER, random.randint(MIN_STEP, MAX_STEP)))
    rand_index = random.randint(0, len(progression) - 5)
    return progression[rand_index:rand_index + random.randint(MIN_LENTH, MAX_LENTH)]


def get_question_and_answer():
    progression = make_progression()
    rand_index = random.randint(0, len(progression) - 1)
    answer = progression[rand_index]
    progression[rand_index] = '..'
    return ' '.join(map(str, progression)), str(answer)

import random

MAX_LENTH = 10
MIN_LENTH = 5
MAX_STEP = 5
MIN_STEP = 1
MAX_NUMBER = 100
MIN_NUMBER = 1

def make_progression():
    rand_int = random.randint(MIN_NUMBER, MAX_NUMBER)
    rand_step = random.randint(MIN_STEP, MAX_STEP)
    rand_lenth = random.randint(MIN_LENTH, MAX_LENTH)
    progression = []
    for i in range(rand_lenth):
        progression.append(rand_int)
        rand_int += rand_step

    return progression

def progression_game():
    progression = make_progression()
    rand_index = random.randint(0, len(progression) - 1)
    answer = progression[rand_index]
    progression[rand_index] = '..'
    return ' '.join(map(str, progression)), str(answer)
import prompt


ROUND_LIMIT = 3


def run(run_game, rule):
    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}!")
    print(rule)

    for _ in range(ROUND_LIMIT):
        question, answer = run_game()
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if str(user_answer) != answer:
            print(f"""'{user_answer}' is wrong answer ;(.
                  Correct answer was '{answer}'.""")
            print(f"Let's try again, {username}!")
            return
        else:
            print("Correct!")
    print(f"Congratulations, {username}!")

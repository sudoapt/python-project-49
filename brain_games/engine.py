import prompt
from brain_games.scripts.congrats import congrats
from brain_games.cli import welcome_user


ROUND_LIMIT_ = 3


def run(game, RULE_):
    username = welcome_user()
    print(RULE_)
    count = 0

    while count < ROUND_LIMIT_:
        question, answer = game()
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if str(user_answer) == answer:
            print("Correct!")
            count += 1
        else:
            print(f"""'{user_answer}' is wrong answer ;(.
                  Correct answer was '{answer}'.""")
            print(f"Let's try again, {username}!")
            break

        congrats(count, ROUND_LIMIT_, username)

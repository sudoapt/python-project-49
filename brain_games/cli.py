import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    username = prompt.string("May i have your name? ")  
    print(f"Hello, {username}")
    return username

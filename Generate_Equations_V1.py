import random


def generate_question():
    number_1 = random.randint(1, 5)
    number_2 = random.randint(1, 10)
    x = random.randint(1, 10)
    answer = number_1 * x + number_2
    equation = f"{number_1}x + {number_2} = {answer}"
    return equation, x


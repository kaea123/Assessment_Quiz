import random


def generate_question():
    number_1 = random.randint(1, 5)
    number_2 = random.randint(1, 10)
    x = random.randint(1, 10)
    answer = number_1 * x + number_2
    equation = f"{number_1}x + {number_2} = {answer}"
    return equation, x


def question_answer_output():
    print("Solve the following equations for x (round your answer to the nearest integer):")
    score = 0
    # Ask user how many questions they'd like to be asked. If they choose otherwise = infinite mode
    num_questions_input = input("How many questions would you like to answer? ")

    while True:
        try:
            num_questions = int(num_questions_input)
            break
        except ValueError:
            print("Invalid input. Please enter a number (integer) of questions you'd like to be asked.")
            num_questions_input = input("How many questions would you like to answer? ")

    game_history = []
    for i in range(num_questions):
        equation, correct_answer = generate_question()
        print(f"\nQuestion {i + 1}: {equation}")
        user_answer = input("Your answer: ")
        try:
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                print("Correct!")
                score += 1
                game_history.append(f"Question {i + 1}: Correct")
            else:
                print(f"Incorrect. The correct answer is {correct_answer}.")
                game_history.append(f"Question {i + 1}: Incorrect")
        except ValueError:
            print("Invalid input. Please enter an integer.")
            game_history.append(f"Question {i + 1}: Invalid input")
    print(f"\nQuiz completed! Your score is {score}/{num_questions}.")
    return score, game_history

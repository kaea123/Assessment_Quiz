# This program is a linear math quiz that generates random linear equations
# and asks the user to solve for x. It keeps track of the user's score and
# provides statistics at the end.

import random


# Function to prompt the user for a yes or no response
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes/no")


# Function to display instructions for the quiz before the game starts
# so the user has a little understanding of the game.
def instructions():
    print('''
**** Instructions **** 

To start begin with, choose the number of questions you would like
to be asked. This quiz does not have the option to either have
0 rounds (which will automatically end the game) or neither has
infinity, so no exit code will be implied too.

The quiz is filled with randomized linear math equations. No questions
in this quiz are equal to a negative number or a decimal place, so
make sure you answer with a positive integer.

Your goal is to answer all the questions and aim for the
highest score by answering all the questions correctly. 
Statistics at the end will display the numbers of questions
that are answered correct, wrong. It will also provide an
average score between the two (correct/wrong).

Your game history will be displayed at the end (on command) showing how many
questions you've gotten right or answered incorrectly. Reminder
that this (the game history) is optional to see.

Best of luck, Yours Truly Kaea.      
''')


# A function to generate a random linear equation
# Numbers that generate (randomly) are between 1 - 10
def generate_question():
    number_1 = random.randint(1, 5)
    number_2 = random.randint(1, 10)
    x = random.randint(1, 10)   # Making sure no questions asked is generated to a negative number and only positive.
    answer = number_1 * x + number_2
    equation = f"{number_1}x + {number_2} = {answer}"  # this is the code where the equation is being asked.
    return equation, x


# Main function/component to run the quiz
def question_answer_output():
    # Print the initial message for the quiz
    print("Solve the following equations for x (round your answer to the nearest integer):")
    score = 0

    # Ask user how many questions they'd like to be asked.
    num_questions_input = input("How many questions would you like to answer? ")

    # Loop to ensure valid input for the number of questions
    while True:
        try:
            num_questions = int(num_questions_input)
            break
        except ValueError:
            # If conversion fails, print an error message and prompt for input again
            print("Invalid input. Please enter a number (positive integer) of questions you'd like to be asked.")
            num_questions_input = input("How many questions would you like to answer? ")

    game_history = []

    for i in range(num_questions):  # Generating a question and it's correct answer. Also get the user's answer.
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
                # If the answer is incorrect, print the correct answer
                print(f"Incorrect. The correct answer is {correct_answer}.")
                game_history.append(f"Question {i + 1}: Incorrect")
        except ValueError:
            # If conversion fails, print an error message
            print("Invalid input. Please enter an integer.")
            game_history.append(f"Question {i + 1}: Invalid input")

    # Print the final score after all questions have been answered
    print(f"\nQuiz completed! Your score is {score}/{num_questions}.")
    return score, game_history  # Return the score and game history


# Main routine
print()
print("📚📚 Linear Math Quiz! 📚📚 ")
print()

# Ask if the user wants to read the instructions
want_instructions = yes_no("Do you want to read the instructions? ")
if want_instructions == "yes":
    instructions()

# Run the quiz
score, game_history = question_answer_output()
all_scores = [score]

# Calculate statistics
all_scores.sort()
correct_score = all_scores[0]
wrong_score = all_scores[-1]
average_score = sum(all_scores) / len(all_scores)

# Output the statistics
print("\n📊📊📊 Statistics 📊📊📊")
print("Here are your statistics on whether you've answered the questions given to you correct or wrong."
      f"\nCorrect: {correct_score} | Wrong: {wrong_score} | Average score: {average_score:.2f}")
print()

# Display the game history on request
see_history = yes_no("Do you want to see your game history? ")
if see_history == "yes":
    for item in game_history:
        print(item)

# End of my game! (A little note to add onto the end)
print("Thank you for you attending my quiz, have an amazing day!")

# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes/no")


def instructions():
    print('''
**** Instructions **** 

To begin, choose the number of questions you would
like to be asked (you may implement an 'infinite' mode 
if you wish).

If you'd want to proceed with 'infinite' mode, after 
reading this message, please press <enter> to continue on
to the following quiz.

The quiz is filled with randomized linear math equations.

Your goal is to answer all the questions and aim for the
highest score by answering all the questions correctly.

Best of luck, Yours Truly Kaea.      
''')


game_history = []
score = 0


# Main routine
print()
print("📚📚 Linear Math Quiz! 📚📚 ")
print()

# Ask if the user wants to read the instructions
want_instructions = yes_no("Do you want to read the instructions? ")
if want_instructions == "yes":
    instructions()

# Run the quiz
all_scores = [score]

# Calculate statistics
correct_score = sum(1 for item in game_history if "Correct" in item)
wrong_score = sum(1 for item in game_history if "Incorrect" in item)
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
else:
    print("🐔🐔🐔 Oops - you chickened out and did not play any rounds. 🐔🐔🐔")

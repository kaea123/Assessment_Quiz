def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes/no")


def instructions():
    print('''
**** Instructions **** 

To start begin with, choose the number of questions you would like
to be asked.

The quiz is filled with randomized linear math equations.

Your goal is to answer all the questions and aim for the
highest score by answering all the questions correctly.

Best of luck, Yours Truly Kaea.      
''')


# Main routine
print()
print("📚📚 Linear Math Quiz! 📚📚 ")
print()

# Ask if the user wants to read the instructions
want_instructions = yes_no("Do you want to read the instructions? ")
if want_instructions == "yes":
    instructions()

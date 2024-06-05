import random


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

# math_test.py
# Exercises selected: Lab 7.4 - Math Test
# Name of program: Math Test
# Description of program: This program will display 10 equations and
#   ask the user to solve each one.  After each the program will
#   identify if the user was correct or incorrect.  At the end of the
#   test the user's results and average score will be displayed.
#
# Ivan Boatwright
# March {insert date}, 2016
import random


def main():
    # Menu control options passed to the menu function.  A list with each
    #   entry a tuple of [0] the display text and [1] the function to call.
    #   Menu numbers start at 1), option 0) defaults to Exit.
    customMenuOptions = [('Enter your name',enter_username),('Take math test', math_test)]

    # Displays the intro to user.
    fluffy_intro()

    # Call the menu loop program.  The menu options are: 1) Average Test
    #   Scores and 0) Exit the program.
    main_menu(customMenuOptions)

    # End main.
    return None


# Section Block: Misc Output ------------------------------------------------>

# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print(page_header('Math Test'))
    print('Welcome! This is a simple math test program.  You are presented\n'
          'ten simple math problems to solve.  After each problem you will\n'
          'be notified if you answered correctly.  When all problems are\n'
          'complete the program will calculate the average correct and\n'
          'displays the results.\n')


# Returns a string used to identify a new part(i.e. page) of the program.
def page_header(title):
    return '{0}\n{1:^40}\n{0}'.format('='*40,title)


# Section Block: Menu ------------------------------------------------------->

# main_menu prints a list of options for the user to select from.  The user
#   enters the desired option's number and the function paired with that
#   option is then executed.  If that option is 0 the while loop is terminated
#   and control returns to the calling function.  Otherwise after the selected
#   function is finished main menu is displayed again.
def main_menu(customMenuOptions):
    # Menu control options. A list with each entry a tuple of
    #   [0] the display text and [1] the function to call.
    menuOptions = [('Exit',exit_menu)]  # Set default menu options.
    menuOptions.extend(customMenuOptions)  # Add custom menu options.
    MENU_COUNT = len(menuOptions)

    # Initialize the loop control variable.
    menuSelection = True

    # While menuSelection does not equal 0 (the default exit option.)
    while menuSelection != 0:
        display_menu(menuOptions)
        # Calls the input request/validation function and converts the return
        #   value into an integer.  The number of menu elements is prepended
        #   to the input request and used as part of the validation testing.
        menuSelection = int(get_valid_inputs([[str(MENU_COUNT) +
                                              ' menu options', 'selection']]))

        # Use the validated user input to select the function reference and
        #   execute the function with the trailing ().
        menuSelection = menuOptions[menuSelection][1]()

    # By design the exit_menu function runs before the while loop breaks.
    return None


# Prints the menu header and menu options to stdout.  The menuOptions list
#   is the parameter and used to generate the option strings.
def display_menu(mOpts):
    print(page_header('Main Menu'))
    # This loops through the list starting at [1] and prints [0] (Exit)
    #   at the end.
    for l in range(1,len(mOpts)):
        print('  {0}) {1}'.format(l, mOpts[l][0]))
    print('  {0}) {1}'.format(0, mOpts[0][0]))
    return None


# Sets the loop control variable to 0 which ends the while loop.
def exit_menu():
    # "Until we meet again, farewell."
    print("\nJusqu'à ce que nous nous reverrons, adieu.")
    return 0


# Section Block: Input Validation ------------------------------------------->

# get_valid_inputs requests input from the user then tests the input.
#   If invalid, it will alert the user and request the correct input.
# The parameter is a nested List of ordered pair Lists.
#   First value is the validation test and second is the user prompt.
def get_valid_inputs(requestsList):
    # local List to hold user inputs for return to calling module
    userInputs = []

    # Loop through each entry in requestsList assigning each List pair
    #  to request.
    for request in requestsList:
        # untestedInput is a holding variable for testing user input validity.
        # First user prompt before testing loop.
        untestedInput = prompt_user_for_input(request[1])

        # If test_value returns True, Not converts it to False and the While
        #   Loop will not execute.
        # If test_value returns False, the While executes and the user is
        #   prompted to enter a valid value.
        while (not test_value(request[0], untestedInput)):

            print('!!! Error: {} is not a valid value.'.format(untestedInput))
            untestedInput = (prompt_user_for_input(request[1]))

        # The user input tested valid and is appended to the userInputs List.
        userInputs.append(untestedInput)
    # for loop terminates and userInputs are returned to calling Module.
    # With only a single test run in this program, only the first value
    #   in userInputs is returned.
    return userInputs[0]


# prompt_user_for_item is passed a String to print to screen as part of a user
#   prompt.  Then returns it to the calling module.
def prompt_user_for_input(promptTerm):
    # promptTerm is a local variable to hold the value passed from the
    #   calling module.
    print('Please enter your {}.'.format(promptTerm))
    return input('  >>> ')


# test_value uses the testCondition to select the proper test.
# It returns True or False to the calling Module.
def test_value(testCondition, testItem):
    # The If-Then-Else structure functions as a Switch for test selection.
    if testCondition[1:] == ' menu options':
        # The number of menu items is prepended to the test condition string.
        #   testCondition[1:] strips the first character and then does the
        #   string comparison.
        # If (the number of menu items) is greater than int(testItem) and
        #   int(testItem) is greater than or equal to zero, True is
        #   returned.  If int(testItem) creates an error or fails the other
        #   logic tests, False is returned.
        try:
            if int(testItem) >= 0 and int(testCondition[:1]) > int(testItem):
                return True
            else:
                return False
        except:
            return False
    else:
        return None


# Section Block: Enter user Name -------------------------------------------->
def enter_username():
    return input('Please enter your name: ')


# Section Block: Math Test -------------------------------------------------->
def math_test():
    # Local variables Dict.
    testData = {
        'qCount': 1,
        'qList': [],
        'operations': ['a'],
        'qMinValue': 0,
        'qMaxValue': 500,
        'qTotal': 10,
        'qCorrect': 0,
        'avgCorrect': 0.0,
        'avgPercent': 0,
    }
    return None

# This randomly generates test questions and stores them in the list reference
#   parameter.  The total number of equations is passed in the qTotal
#   variable. Optionally a list of operations can be supplied for a wider
#   question variety.  The default operation is addition.
def generate_test_questions(qList, ops=('a',), qTotal=10):
    for q in range(qTotal):
        op = random.choice(ops)
        rVals = generate_numbers()
        qList[q] = (rVals[0], rVals[1], operate(op, rVals))
    return None

def operate(ops, rVals):



# Simple random number generator.  Optional parameters specify minimum/maximum integer
#   values selected and how many values to return.
def generate_numbers(min=0, max=500, xNums=2):
    # Uses the sample function from the random module to generate a list of
    #   integers.  The range function is used with the min and max variables
    #   to set the possible integer values generated.
    return random.sample(range(min, max), xNums)



# Calculates the average of two numbers and return the value.  Optionally
#   specify how many decimal places are returned.  If percent is True or if
#   there is no fractional component, the value is converted to an integer
#   and returned.
def calc_average(sum, count, precision=2, percent=False):
    avg = round(sum / count, precision)
    if percent or sum % count == 0:
        avg = int(avg)
    return avg


# display_results is passed values used in print statements to display
#  the results of the program to the user.
def display_results(userName, count, total, avg, avgP):
    print(page_header('Math Test Results'))
    print('{}'.format(userName))
    print('You answered {0} correct out of {1} questions.'.format(count,
                                                                  total))
    print('Your average correct is: {0} or {1}'.format(avg, avgP))
    print('\n\n')
    return None


# Start the program
main()
# Rock-paper-scissors-lizard-Spock template
import random


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if (name == "rock"):
        choice_num = 0
    elif (name == "Spock"):
        choice_num = 1
    elif (name == "paper"):
        choice_num = 2
    elif (name == "lizard"):
        choice_num = 3
    elif (name == "scissors"):
        choice_num = 4
    else:
        Print("Error: Name doesn't match")
    return (choice_num)



    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if (number == 0):
        choice_name = "rock"
    elif (number == 1):
        choice_name = "Spock"
    elif (number == 2):
        choice_name = "paper"
    elif (number == 3):
        choice_name = "lizard"
    elif (number == 4):
        choice_name = "scissors"
    else:
        print("Error : Not a valid number")
    return (choice_name)

    # convert number to a name using if/elif/else
    # don't forget to return the result!


def rpsls(player_choice):
    # delete the following pass statement and fill in your code below
    player_num = name_to_number(player_choice)
    print ("Player chooses ", player_choice)
    comp_num = random.randrange(0, 5)
    comp_choice = number_to_name(comp_num)
    print ("Computer chooses ", comp_choice)
    result = (player_num - comp_num) % 5
    if (result == 0):
        print ("Player and computer tie!")
    elif (result == 1 or result == 2):
        print("Player wins!")
    else:
        print("Computer wins!")
    print ("")


    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()

    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



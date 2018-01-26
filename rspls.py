# This program implements the Rock-paper-scissors-lizard-Spock game. Each choice wins against two other choices,
# loses against two other choices and ties against itself. 

import random

def name_to_number(name):
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
   
def number_to_name(number):
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

def rpsls(player_choice):
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
   
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




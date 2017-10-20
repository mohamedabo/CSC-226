######################################################################
# Author: Dr. Scott Heggen              TODO: Abdirahman Mohamed
# Username: heggens                     TODO: mohameda
#
# Assignment: A5:  The Game of Nim
# Purpose: # Practice breaking a larger problem down into smaller "mental chunks"using functions
            # Gain practice using loops and modulus (%)

######################################################################
# #################################################################################
import random
player1=str(input("Enter your name"))
player2="Computer"


def initial_number():
    init_num = 0
    while init_num <= 15:
        init_num = int(input("Welcome to the Game of Nim! How many balls would you like to start?"))
        if init_num < 15:
            print("Pick a number between 15 or higher")
        else:
            return init_num
        print("Now you are playing against the computer! You will go first")
def player_choice ():
    init_num = 0
    while init_num <1 or init_num>4:
        init_num = int(input("Choose between 1 or 4 balls to draw"))

        if init_num <1 or init_num>4 :
            print("Pick a number between 1 and 4")
        else:
            return init_num

def computer_choice (num):
    check = num%5
    if check == 0:

        num = random.randint(1,4)
        print(num)
        return num
    else:
        return check

def main():
    num = initial_number()
    check = True
    while num != 0:
        print("There are " + str(num) + " balls left")
        num = num - player_choice()
        if num == 0:
            break
        num= num- computer_choice(num)
        if num == 0:
            check = False
    if check:
          print("You Won! Mabrouk!")

    else:
        print("You lost! Good luck next time!")

    

main()










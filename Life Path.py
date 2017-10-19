######################################################################
# Author: Abdirahman Mohamed
# Username:  mohameda
#
# Assignment: A4:  A Bug's Life
# Purpose: Learn the impact a bug can have in the real world. Explore life path numbers. Practice creating your own fruitful functions and Learn to use modulus to capture remainders

######################################################################
# #################################################################################

def Cal(Val):
    """ It calculates the value of the sum of the digits  """
    CAL = int(0)
    for i in Val:
        CAL = CAL + (int(i))
    return(CAL)

def main ():
    """Definiton of varibles and calculating the life path number"""
    m = input("What month were you born?")
    d = input("What day were you born?")
    y = input ("What year were you born?")

    print(Cal(m))
    print(Cal(d))
    print(Cal(y))
    sum = Cal(m) + Cal(d) + Cal (y)
    print(sum)
    Master = sum % 11
    if Master == 0:      #If the number was divisible by 11 then it is true.
        life_path_number =  Master
    else:    #If it is not divisible by 11, then it is false.
        life_path_number = Cal(str(sum))

    print(life_path_number)
    if life_path_number == 1:
        print("You are a Leader! You won't be like Puyol but you are leader anyways lol")
    elif life_path_number == 2:
        print("You are a Mediator! Not sure what it means but be happy")
    elif life_path_number == 3:
        print("You are a Communicator! Apperntly you like to talk to people")
    elif life_path_number == 4:
        print("You are a Teacher! Still making less than a mail man")
    elif life_path_number == 5:
        print("You are a Freedom Seeker! Way to go Che Guevara")
    elif life_path_number == 6:
        print("You are a Nurturer! So cool")
    elif life_path_number == 7:
        print("You are a Seeker! You should be proud")
    elif life_path_number == 8:
        print("You are a Powerhouse! So strong")
    elif life_path_number == 9:
        print("You are a Humantarian! I salute you")
    else:
        print("Congratulations! You are different! You are unique!")


main()










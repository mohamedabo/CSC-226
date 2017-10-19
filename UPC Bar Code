######################################################################
# Author: Abdirahman Mohamed
# Username: mohameda
#
# Assignment: A7: UPC Barcode
#
# Purpose: Learn about an important application of computer science, the UPC code
#Work on the design of a larger problem
#Use lists in an application problem

#
######################################################################
"""
This program takes the input,checks its length,turn it to binary numbers then calculate the sum then draws the bar code
        """
import random
import turtle
import sys
def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """

    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
def convert (enter):
    """Takes the input number and appened it to an empty list"""
    UPC_list= []    # Empty list that would appened the input
    for i in enter:
        UPC_list.append(i)
    print(UPC_list)
    return UPC_list



def check_user_input(enter):
    """This function checks whether the input is True or False"""
    if len(enter)!=12:   #Conditional statement to determain whether length of enter is not equal to 12
        return False
    else:
        return True
def modulo_check_character(list):
    """This function calculates total sum"""
    odd_sum = 0   # odd sum is equal to zero
    even_sum = 0  # even sum is equal to zero
    for i in range (len(list)):
        if (i%2 == 0):  # Conditional to determain if the number is even and calcualte its sum
            even_sum+=int(list[i])

        else:    # Calculates the sum of odd number
            odd_sum+=int(list[i])


    total_sum= (odd_sum*3)+ even_sum
    print(total_sum)
    mod = total_sum%10
    check_digit=10-mod
    if check_digit==int(list[-1]):
        return True
    else:
        return False
def decimal_to_binary(list):
    """Converts the input numbers into binary numbers"""
    Left = list[0:6]  # Setting left side of numbers
    Right = list[6:12] # Setting right side of numbers
    Converted_Left = [] # Setting an empty string for the left side of numbers
    Converted_Right = [] # Setting an empty string for the right side of numbers
    for i in Left:
        if int(i) == 0:
            Converted_Left.append("0001101")
        elif int(i) == 1:
            Converted_Left.append("0011001")
        elif int(i) == 2:
            Converted_Left.append("0010011")
        elif int(i) == 3:
            Converted_Left.append("0111101")
        elif int (i) == 4:
            Converted_Left.append("0100011")
        elif int (i) == 5:
            Converted_Left.append("0110001")
        elif int (i) == 6:
            Converted_Left.append("0101111")
        elif int (i) == 7:
            Converted_Left.append("0111011")
        elif int (i) == 8:
            Converted_Left.append("0110111")
        elif int (i) == 9:
            Converted_Left.append("0001011")
    for i in Right:
        if int(i) == 0:
            Converted_Right.append("1110010")
        elif int(i) == 1:
            Converted_Right.append("1100110")
        elif int(i) == 2:
            Converted_Right.append("1101100")
        elif int(i) == 3:
            Converted_Right.append("1000010")
        elif int (i) == 4:
            Converted_Right.append("1011100")
        elif int (i) == 5:
            Converted_Right.append("1001110")
        elif int (i) == 6:
            Converted_Right.append("1010000")
        elif int (i) == 7:
            Converted_Right.append("1000100")
        elif int (i) == 8:
            Converted_Right.append("1001000")
        elif int (i) == 9:
            Converted_Right.append("1110100")


    print(Converted_Left)
    print (Converted_Right)
    return(translate(Converted_Left,Converted_Right))

def translate (Converted_Left,Converted_Right):
    """Translate the binary numbers in right and left sides to include the guard and center numbers of the bar code"""
    output = ""   # Empty string
    output = output + '010'
    for i in Converted_Left:
        output = output + i
    output = output+'01010'
    for i in Converted_Right:
        output = output + i
    output = output + '010'

    print(output)
    return(output)

def draw_barcode(t,completed_barcode,enter):
    """Draws the bar code"""
    for i in completed_barcode[0:10]:  #The first 10 binary digits
        if int(i)==0:
            t.color("White")
        else:
            t.color("Black")

        t.pensize(2)
        t.left(90)
        t.pendown()
        t.forward(100)
        t.penup()
        t.backward(100)
        t.right(90)
        t.forward(2)


    for i in completed_barcode[10:45]: # From the 10th binary digits to 45th binary digits
        if int(i)==0:
            t.color("White")
        else:
            t.color("Black")

        t.pensize(2)
        t.left(90)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(90)
        t.backward(90)
        t.penup()
        t.backward(10)
        t.right(90)
        t.forward(2)
        t.pendown()
    for i in completed_barcode[45:50]:  # From the 45th binary digit to 50th binary digits
        if int(i)==0:
            t.color("White")
        else:
            t.color("Black")

        t.pensize(2)
        t.left(90)
        t.pendown()
        t.forward(100)
        t.penup()
        t.backward(100)
        t.right(90)
        t.forward(2)
    for i in completed_barcode[50:85]:  # From 50th binary digit to 85th binary digit
        if int(i)==0:
            t.color("White")
        else:
            t.color("Black")

        t.pensize(2)
        t.left(90)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(90)
        t.backward(90)
        t.penup()
        t.backward(10)
        t.right(90)
        t.forward(2)
        t.pendown()
    for i in completed_barcode[85:95]: # From the 85th binary digit to 95th binary digit
        if int(i)==0:
            t.color("White")
        else:
            t.color("Black")
        t.pensize(2)
        t.left(90)
        t.pendown()
        t.forward(100)
        t.penup()
        t.backward(100)
        t.right(90)
        t.forward(2)

        t.write(enter, move=False, align="right", font=("Arial", 20, "normal"))





















def main ():
    """Takes the input,checks if its length equals to 12 and then turn it to binary then draws its bar code"""

    enter = input("Enter 12 digit number")
    while len(enter)!=12:
        enter = input("Error! Please Enter 12 digit number")
        if len(enter)==12:
            break

    list =convert(enter)


    check_user_input(enter)
    print(modulo_check_character(list))
    completed_barcode = decimal_to_binary(list)
    t= turtle.Turtle()
    wn=turtle.Screen()
    wn.bgcolor("White")
    wn.delay(0)

    print(completed_barcode)
    draw_barcode(t,completed_barcode,enter)
    wn.exitonclick()












main()









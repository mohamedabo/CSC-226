######################################################################
# Author: Abdirahman Mohamed
# Username: mohameda
#
# Assignment: A9: XHTML
#
# Purpose: Work with both input and output files
#Gain additional practice working with strings
#Learn a bit about web page structure

####################################################################################
def open_the_file():
    filename = input("Enter the filename: ")
    try:
        file = open(filename, "r")
        my_file = file.readlines()
        return my_file
    except:
        print("Invalid file name")


def checking_lines(file):

    print(file)
    """for i in range(0, len(file)):
        line = file[i]
        for j in range(len(line)):
            if line[j:j+4]=="meta":
                line = line[0:len(line)] + " />" + "\n"
                print(line)"""


def main():

   a = open_the_file()
   checking_lines(a)
main()


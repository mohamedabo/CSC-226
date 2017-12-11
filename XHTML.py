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
    """Opens the file and read it if it is correct. If not, it will print invalid file name"""
    filename = input("Enter the filename: ")   #Enter the name of the file
    try:
        file = open(filename, "r")   #Opens the file and reads it
        my_file = file.readlines()    #Reading all lines of filee
        return my_file
    except:
        print("Invalid file name")  #Print invalid if filename is not correct


def checking_lines(file):
    """Checks every line, adds / to the last element and count the changes on each catagory"""
    meta = 0
    img = 0
    br = 0
    hr = 0
    for i in range(0, len(file)):
        line = file[i]
        for j in range(len(line)):
            if line[j:j+4]=="meta" or line[j:j+3]=="img" or line[j:j+2]=="br" or line[j:j+ 2]=="hr":
                line = line[0:len(line)-2] + " />" + "\n" #Adds /> to the last line of every elemnt
                file[i] = line
            if line[j:j+4]=="meta":
                meta += 1  #Counts how many changes in meta
            elif line[j:j+3]=="img":
                img += 1   #Counts how many changes in img
            elif line[j:j+2]=="br":
                br += 1    #Counts how many changes in br
            elif line[j:j+ 2]=="hr":
                hr += 1    #Counts how many changes in hr


    print("You have done " + str(meta) + ' changes to meta')
    print("You have done " + str(img) + ' changes to img')
    print("You have done " + str(br) + ' changes to br')
    print("You have done " + str(hr) + ' changes to hr')

    return file    #Returning file


def write(file):
    """Writes the new file"""
    new_file = input("Write the name of your new file") #Enter name of file you want to create
    f = open(new_file, 'w')  #open the file and write it
    f.writelines(file)  #Writing lines in new file


def main():
   """Make changes to old file by creating new file that adds /> to the last element. Also, it counts how many times changes have been made to img,br,hr and meta """

   a = open_the_file() #varible a equals function open_the_file to use it as a parameter for checking_lines
   b = checking_lines(a) #varible b equals function checking_lines to use it as a parameter for write function
   write(b)
main() #Call to main


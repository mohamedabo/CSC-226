######################################################################
# Author:Abdirahman Mohamed
# Username:mohameda
#
# Assignment: A8: Error Detection
#
# Purpose: More practice breaking a larger problem down into smaller pieces using functions
#Gain practice using strings
#Introduce concepts about binary and parity

#
######################################################################
#
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import sys
def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
def parity_test_suite():
    print("\nTesting is_binary(enter)")
    testit(is_binary ("0120000") == False)
    testit(is_binary("0101010") == True)
    testit(is_binary("0011001") == True)
    testit(is_binary("0101019") == False)

    print("\nTesting is_div_by_sevens(enter)")
    testit(is_div_by_sevens("012000000") == False)
    testit(is_div_by_sevens("0101110") == True)
    testit(is_div_by_sevens("0111001") == True)
    testit(is_div_by_sevens("01010190") == False)

    print("\nTesting is_div_by_sevens(enter)")
    testit(is_div_by_sevens("0111001011100101110010111001") == True)
    testit(is_div_by_sevens("010111001011100101110") == True)
    testit(is_div_by_sevens("01110010111001") == True)
    testit(is_div_by_sevens("0101011") == True)

    print("\nTesting split_into_sevens(enter)")
    testit(split_into_sevens("0101010") == ['0101010'])
    testit(split_into_sevens("01011000000000") == ['0101100','0000000'])
    testit(split_into_sevens("011100101110010111001") == ['0111001','0111001','0111001'])
    testit(split_into_sevens("0101011010101101010110101011") == ['0101011','0101011','0101011','0101011'])






def is_binary(enter):
    """Checks whether enter is a binary number of 0 and 1"""
    variable = False
    for i in range (len(enter)):
        if enter[i]=="0" or enter[i]=="1":
            variable= True

        else:
            return False
    return variable



def is_div_by_sevens(enter):
    if len(enter)%7==0:
        return True
    else:
        return False
def split_into_sevens(enter):
    string = []
    for i in range (len(enter)//7):
        string.append(enter[i*7:i*7+7])
    #del string[0]
    print(string)
    return string







def main():
    """"""
    enter = input("Enter 7 binary number of 0 and 1")


    is_binary(enter)
    is_div_by_sevens(enter)
    print(is_binary(enter))
    print(is_div_by_sevens(enter))
    split_into_sevens(enter)
    print(split_into_sevens(enter))
    chunck = split_into_sevens(enter)
    for i in range (len(chunck)):
        sum = 0
        bit = chunck[i]
        for a in range(len(bit)):
            sum+=int(bit[a])
        if sum%2==0:
            chunck[i]= "0" + chunck[i]
        else:
            chunck[i]== "1" + chunck[i]
    print(chunck)
    parity_test_suite()





if __name__ == '__main__':


    main()





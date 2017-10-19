######################################################################
# Author: Dr. Scott Heggen      TODO: Abdirahman Mohamed
# Username: heggens             TODO: mohameda
#
# Assignment: A1
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1984 and 1995. Also returns your compatibility
# with other animals.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Task 1
# TODO Ask user for their birth year
user_birthyear = int(input("What is your birth year?"))

if user_birthyear == 1984 or user_birthyear == 1972 or user_birthyear == 1996:
    print (("You are a Rat!"))
elif user_birthyear == 1985 or user_birthyear == 1973 or user_birthyear == 1997:
    print ("You are an Ox!")
elif user_birthyear == 1974 or user_birthyear == 1986 or user_birthyear == 1998:
    print ("You are a Tiger!")
elif user_birthyear == 1975 or user_birthyear == 1987 or user_birthyear == 1999:
    print ("You are a Rabbit!")
elif user_birthyear == 1976 or user_birthyear == 1988 or user_birthyear == 2000:
    print ("You are a Dragon!")
elif user_birthyear == 1977 or user_birthyear == 1989 or user_birthyear == 2001:
    print ("You are a Snake!")
elif user_birthyear == 1978 or user_birthyear == 1990 or user_birthyear == 2002:
    print("You are a Horse!")
elif user_birthyear == 1979 or user_birthyear == 1991 or user_birthyear == 2003:
    print("You are a Goat!")
elif user_birthyear == 1980 or user_birthyear == 1992 or user_birthyear == 2004:
    print("You are a Monkey!")
elif user_birthyear == 1981 or user_birthyear == 1993 or user_birthyear == 2005:
    print("You are a Rooster!")
elif user_birthyear == 1982 or user_birthyear == 1994 or user_birthyear == 2006:
    print("You are a Dog!")
elif user_birthyear == 1983 or user_birthyear == 1995 or user_birthyear == 2007:
    print("You are a Pig!")
# TODO Check the year, print the correct animal for that year

# Task 2
# TODO Ask the user for their friend's birth year
your_friends_birth_year= int(input("What is your friend's birth year?"))
friend_zodiac = 0
if your_friends_birth_year == 1984 or your_friends_birth_year == 1972 or your_friends_birth_year == 1996:
    print (("You are a Rat!"))
    print("No match!")
elif your_friends_birth_year == 1985 or your_friends_birth_year == 1973 or your_friends_birth_year == 1997:
    print ("You are an Ox!")
    print("No match!")
elif your_friends_birth_year == 1974 or your_friends_birth_year == 1986 or your_friends_birth_year == 1998:
    print ("You are a Tiger!")
    print("Best match!")
    friend_zodiac = "Tiger"
elif your_friends_birth_year == 1975 or your_friends_birth_year == 1987 or your_friends_birth_year == 1999:
    print ("You are a Rabbit!")
    print("Best match!")
    friend_zodiac = "Rabbit"
elif your_friends_birth_year == 1976 or your_friends_birth_year == 1988 or your_friends_birth_year == 2000:
    print ("You are a Dragon!")
    print("No match!")
elif your_friends_birth_year == 1977 or your_friends_birth_year == 1989 or your_friends_birth_year == 2001:
    print ("You are a Snake!")
    print("No match!")
    friend_zodiac = "Snake"
elif your_friends_birth_year == 1978 or your_friends_birth_year == 1990 or your_friends_birth_year == 2002:
    print("You are a Horse!")
    print("No match!")
elif your_friends_birth_year == 1979 or your_friends_birth_year == 1991 or your_friends_birth_year == 2003:
    print("You are a Goat!")
    print("Best match!")
    friend_zodiac = "Goat"
elif your_friends_birth_year == 1980 or your_friends_birth_year == 1992 or your_friends_birth_year == 2004:
    print("You are a Monkey!")
    print("No match!")
elif your_friends_birth_year == 1981 or your_friends_birth_year == 1993 or your_friends_birth_year == 2005:
    print("You are a Rooster!")
    print("No match!")
elif your_friends_birth_year == 1982 or your_friends_birth_year == 1994 or your_friends_birth_year == 2006:
    print("You are a Dog!")
    print ("No match!")
elif your_friends_birth_year == 1983 or your_friends_birth_year == 1995 or your_friends_birth_year == 2007:
    print("Okay Match!")
    friend_zodiac = "Pig"





# TODO Check the year, print the correct animal for that year


my_birth_year = 1995       # TODO change this to your birth year

# Task 3
# TODO Check for compatibility between two birth years
if friend_zodiac == "Snake":
    print("We are not a match because snakes makes me terrified")
if friend_zodiac == "Tiger" or friend_zodiac == "Rabbit" or friend_zodiac == "Goat":
    print("We are a strong match becuase we look cute together")
if friend_zodiac == "Pig":
    print("We are an in between match (okay match) becuase you like Futbol Club Barcelona!")
else:
    print("No Match! Sorry!")





# NOTE: You can assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between



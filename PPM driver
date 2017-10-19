######################################################################
# Author: Dr. Scott Heggen      TODO: Abdirahman Mohamed
# Username: heggens             TODO: mohameda
#
# Assignment: A11: PPM
#
# Purpose: Navigating large code bases
#Working with classes, particularly creating new methods and calling them
#Explore different image encoding methods, and understand how computers represent images

# ######################################################################
# Acknowledgements:
#
# Original code written by Dr. Jan Pearce
#
# Ben Stephenson: http://pages.cpsc.ucalgary.ca/~jacobs/Courses/cpsc217/W10/code/Topic7/ppm.py
# working from a class: http://bytes.com/topic/python/answers/520360-trouble-displaying-image-tkinter
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

from ppm_mohameda import *



def main():
    # The following interaction is just for testing.  You will improve this.

    wn = PPM_set_up()   # To use the PPM class, this must appear at the beginning of your program. You'll pass wn into
                        # the class init method when creating new PPM objects

    print("\nWelcome to the PPM introduction!\n")

    # Example using the default file
    ppmdefault = PPM(wn)
    ppmdefault.PPM_display()            # NOTE: This displays the image, but it's really small! It may be hard to find.
    print("---")

    # Example using a user-defined file
    filename = input("Please input name of PPM-P3 file: ") # user input
    ppmobject = PPM(wn, filename)
    ppmobject.PPM_make_red() # color would be red
    ppmobject.PPM_grayscale() # color would be gray
    ppmobject.PPM_flip_horizontal()
    ppmobjecttwo = PPM(wn, filename) # creating another object
    ppmobjecttwo.PPM_rotateclockwise()  # call to rotate clockwise
    ppmobjecttwo.PPM_make_green()  #The new method I have implemented and it is color green
    ppmobject.PPM_display() # display first object
    ppmobjecttwo.PPM_display() # display second object






    print("\nPush the Quit button to exit all files.")

    PPM_render(wn) # needed to render all of the images you have instantiated
    pass

main()

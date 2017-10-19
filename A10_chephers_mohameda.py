######################################################################
# Author: Dr. Scott Heggen      TODO: Abdirahman Mohamed
# Username: heggens             TODO: mohameda
#
# Assignment: A10: Caesar Cipher
#
# Purpose: The class imports a file, encrypts the file, and exports the cipher to a new file
#           You need to implement the decrypt function.
######################################################################
# Acknowledgements:
#
# Acknowledgements: The original code was created by Dr. Scott Heggen
#                       and modified by Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import sys

class CaesarCipher:
    """Class to define method """

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"            # The alphabet, which will be used to do our shifts

    def __init__(self, input_file = "message_input.txt", key = 0, crypt_type = "encrypt"):
        """
        A constructor for the CaesarCipher class

        :param input_file: The file to be encrypted/decrypted
        :param key: The amount each message/cipher needs shifted
        :param crypt_type: Either encrypt or decrypt
        """
        self.input_file = input_file                            # The file to be encrypted or decrypted
        self.key = key                                          # The amount each message/cipher will be shifted
        self.message = ""                                       # A placeholder for the message
        self.cipher = ""                                        # A placeholder for the cipher
        self.crypt_type = crypt_type                            # Either "encrypt" or "decrypt"
        self.import_file()                                      # Calls the import_file() method below


    def import_file(self):
        """
        Imports a file stored in the variable self.input_file

        :return: a string representing the contents of the file
        """
        f = open(self.input_file, "r")
        if self.crypt_type == "encrypt":
            self.message = f.read()                  # Set self.message to the file contents
        elif self.crypt_type == "decrypt":
            self.cipher = f.read()                   # Set self.cipher to the file contents
        f.close()

    def export_file(self, text_to_export, filename):
        """
        Exports a file called filename

        :param text_to_export: the string to be written to the exported file
        :param filename: a string representing the name of the file to be exported to
        """
        f = open(filename, "w")
        f.write(text_to_export)
        f.close()
        print("File exported to " + filename)

    def encrypt(self):
        """
        Converts an original message into a ciphered message with each letter shifted to the right by the key
        :return: a string representing the ciphertext
        """
        output = ""
        for i in self.message:
            if i.upper() in self.alphabet:
                old_letter = self.alphabet.find(i.upper())
                # Uses modulus to return the correct index for each letter after the shift
                # (for cases where the index is outside the range of self.alphabet,
                #  it wraps back to the beginning of the alphabet)
                output += self.alphabet[(old_letter + self.key) % 26]
            else:
                output += i         # Adds non-alphabet characters directly
        return output


    def decrypt(self):
        """
        Converts a ciphertext into an original message by shifting each letter to the left by the key

        :return: a string representing the original message
        """

        output = ""
        for i in self.cipher:
            if i.upper() in self.alphabet:
                old_letter = self.alphabet.find(i.upper())
                output += self.alphabet[(old_letter - self.key) % 26]
            else:
                output += i         # Adds non-alphabet characters directly
        return output



def main():
    '''Exports three files, two of them encrypted and the other one is decrypted'''


    # Caesar has some letters to send and receive.



    cipher1 = CaesarCipher("letter_to_friend_1.txt", 3, "encrypt")   # Constructs a new CaesarCipher object called cipher1
    cipher_text1 = cipher1.encrypt() # Encrypts the file specified in the constructor
    cipher1.export_file(cipher_text1, "cipher_to_friend_1.txt")   # Writes the output to a file





    # Letter 2 is coming from Caesar to Ciero to decrypt. They use key 14
    cipher2 = CaesarCipher("letter_to_friend_2.txt", 14, "encrypt")   # Constructs a new CaesarCipher object called cipher2
    cipher_text2 = cipher2.encrypt() # Encrypts the file specified in the constructor
    cipher2.export_file(cipher_text2, "cipher_to_friend_2.txt") # Writes the output to a file


    # Letter 3 is coming from Cicero for Caesar to decrypt. Again, they agreed to use key 14
    cipher3 = CaesarCipher("letter_from_friend_3.txt", 14, "decrypt")
    cipher_text3= cipher3.decrypt()# constructs a new CaesarCipher object called cipher3
    cipher3.export_file(cipher_text3,"message_from_friend_3.txt")

if __name__ == "__main__":
    main()

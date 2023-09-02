##########################################################################################
#                                                                                        #
# File: ASCII.py                                                                         #
# Author: Mohamed Samy Ahmed                                                             #
# Date: August 8, 2023                                                                   #
#                                                                                        #
# Description:                                                                           #
#    Provide a brief description of the purpose and functionality of the Python file.    #
#                                                                                        #
##########################################################################################

def get_ascii_code(character):
    ascii_code = ord(character)
    return ascii_code

input_character = input("Enter a character: ")
while len(input_character) != 1:
    print("Please enter only one character.")
    input_character = input("Enter a character: ")

ascii_value = get_ascii_code(input_character)
print(f"The ASCII code of '{input_character}' is {ascii_value}.")
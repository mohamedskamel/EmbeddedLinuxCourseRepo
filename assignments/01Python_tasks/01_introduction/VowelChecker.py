#########################################################################################################################
#                                                                                        			                	#
# File: VowelChecker.py                                                                    			                	#
# Author: Mohamed Samy Ahmed                                                                     			            #
# Date: August 11, 2023                                                                   			                	#
#                                                                                        			                	#
# Description:                                                                           			                	#
#    checking for the input character is a vowel or not                                 			                	#
#                                                                                        			                	#
#########################################################################################################################
#!/usr/bin/python3

#List of vowels
Vowel = ['A','E','I','O','U']

#get the input character
Char = input("Enter the char please: ")

#check the input with the vowel set
if Char.upper() in Vowel :
    print("The entered Char is a Vowel")
else :
    print("The entered Char is NOT a Vowel")

#########################################################################################################################
#                                                                                        			                	#
# File: OccurrenceOfNum4InList.py                                                                       			    #
# Author: Mohamed Samy Ahmed                                                                     			            #
# Date: August 11, 2023                                                                   			                	#
#                                                                                        			                	#
# Description:                                                                           			                	#
#    This Program calculates the number of occurrences of number 4 in a given list by user     			                #
#                                                                                        			                	#
#########################################################################################################################
#!/usr/bin/python3

#get the List from the user
Input_list = input("Please enter your list separated by comma ")

#convert the input into a list
Input_list = Input_list.split(",")

#print the counter
print(Input_list.count('4'))



#########################################################################################################################
#                                                                                        			                	#
# File: example.py                                                                       			                	#
# Author: Your Name                                                                      			                	#
# Date: August 8, 2023                                                                   			                	#
#                                                                                        			                	#
# Description:                                                                           			                	#
#    Provide a brief description of the purpose and functionality of the Python file.    			                	#
#                                                                                        			                	#
#########################################################################################################################
#!/usr/bin/python3

#include Math Module to get PI Value and power function
import math

#get the Radius from the User
radius=(float) (input("Enter The Radius in cm : "))

#Area Calculations 
area=math.pi*math.pow(radius,2)

print(f"Area is '{area}' cm Squares")


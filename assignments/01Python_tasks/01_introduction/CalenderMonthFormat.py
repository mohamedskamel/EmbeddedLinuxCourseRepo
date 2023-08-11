#########################################################################################################################
#                                                                                        			                	#
# File: CalenderMonthFormat.py                                                                       			        #
# Author: Mohamed Samy Ahmed                                                                      			            #
# Date: August 11, 2023                                                                   			                	#
#                                                                                        			                	#
# Description:                                                                           			                	#
#    This program returns the formate of the calender for any given month          .    			                	#
#                                                                                        			                	#
#########################################################################################################################
#!/usr/bin/python3

import calendar

# initializing the year and month
Date = input("PLease Enter The date in the following format MM/YY : ")
Date = Date.split("/")

# printing the calendar
print(calendar.month(int(Date[1]), int(Date[0])))


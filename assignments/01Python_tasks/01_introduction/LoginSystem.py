#########################################################################################################################
#                                                                                        			                	#
# File: LoginSystem.py                                                                       			                #
# Author: Mohamed Samy Ahmed                                                                     			            #
# Date: August 11, 2023                                                                   			                	#
#                                                                                        			                	#
# Description:                                                                           			                	#
#    Program that can handle simple login system with predefined credentials.           			                	#
#                                                                                        			                	#
#########################################################################################################################
#!/usr/bin/python3

#making directory contains the predefined credentials
data_base = {
    "Ahmed":"1394",
    "Ali":"6078",
    "Amr":"9345"
}

#get user info
Username = input("Enter your Username :")
Password = input("Enter your Password :")


if Username in data_base.keys():
    
    #check the password matches our database
    if Password in data_base[Username]:
        print("Welcome user")
    else:
        print("Invalid credentials")
        
else:
    print("Invalid credentials")

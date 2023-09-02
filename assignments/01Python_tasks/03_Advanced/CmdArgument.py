##########################################################################################
#                                                                                        #
# File: CmdArgument.py                                                                   #
# Author: Mohamed Samy Ahmed                                                             #
# Date: August 8, 2023                                                                   #
#                                                                                        #
# Description:                                                                           #
#    Provide a brief description of the purpose and functionality of the Python file.    #
#                                                                                        #
##########################################################################################

import sys

def count_command_line_arguments():
    arguments = sys.argv[1:]
    return len(arguments)

def get_command_line_arguments():
    arguments = sys.argv[1:]  # Exclude the script name
    return arguments

arg_num = count_command_line_arguments()

if arg_num != 0:
    print("Number of arguments:", arg_num)
    args = get_command_line_arguments()
    print("Command-line arguments:", args)
else :
    print("Command-line arguments are EMPTY")
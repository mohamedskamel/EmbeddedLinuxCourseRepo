#########################################################################################################################
#                                                                                        			                	#
# File: getEnvironmentVariables.py                                                         			                	#
# Author: Mohamed Samy Ahmed                                                                     			            #
# Date: August 11, 2023                                                                   			                	#
#                                                                                        			                	#
# Description:                                                                           			                	#
#    get the environment variables of the OS                                               			                	#
#                                                                                        			                	#
#########################################################################################################################
#!/usr/bin/python3

import os

#get the environment variables and their values by the dict. obtained by os library
for EnvVariable, value in os.environ.items():
    print('-'*24)
    print(f"{EnvVariable} = {value}")
print('-'*24)
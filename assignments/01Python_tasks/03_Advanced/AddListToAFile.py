##########################################################################################
#                                                                                        #
# File: GetLocationByIP.py                                                                   #
# Author: Mohamed Samy Ahmed                                                             #
# Date: August 8, 2023                                                                   #
#                                                                                        #
# Description:                                                                           #
#    Provide a brief description of the purpose and functionality of the Python file.    #
#                                                                                        #
##########################################################################################
def write_list_to_file(file_path, input_list):
    try:
        with open(file_path, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print("List written to the file successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
my_list = ['apple', 'banana', 'cherry', 'date']
file_path = 'output.txt'
write_list_to_file(file_path, my_list)
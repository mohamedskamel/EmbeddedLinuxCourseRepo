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


def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            num_words = len(words)
            return num_words
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    count = count_words(file_path)
    if count is not None:
        print(f"Number of words in the file: {count}")
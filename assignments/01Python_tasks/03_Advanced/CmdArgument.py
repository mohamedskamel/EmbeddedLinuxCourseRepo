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
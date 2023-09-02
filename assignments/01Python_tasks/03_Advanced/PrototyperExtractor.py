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


import re
from openpyxl import Workbook

def parse_header_file(header_file_path):
    function_prototypes = []
    pattern = r'\b\w+\s+\w+\(.*?\);'  # Regular expression to match function prototypes

    with open(header_file_path, 'r') as file:
        content = file.read()
        matches = re.findall(pattern, content)
        for match in matches:
            function_prototypes.append(match.strip())

    return function_prototypes

def insert_into_excel(function_prototypes):
    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "ID"
    sheet["B1"] = "Function Prototype"

    for idx, prototype in enumerate(function_prototypes):
        row = idx + 2  # Start from row 2
        cell_id = f"A{row}"
        cell_prototype = f"B{row}"
        sheet[cell_id] = f"IDX{idx}"
        sheet[cell_prototype] = prototype

    workbook.save("function_prototypes.xlsx")
    print("Function prototypes inserted into Excel sheet successfully.")

# Example usage
header_file_path = "example_header.h"
prototypes = parse_header_file(header_file_path)
insert_into_excel(prototypes)
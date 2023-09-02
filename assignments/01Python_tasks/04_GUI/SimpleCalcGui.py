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

import tkinter as tk

def calculate_sum():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Sum: {result}")
    except ValueError:
        result_label.config(text="Invalid input!")

# Create the main window
window = tk.Tk()
window.title("Sum Calculator")

# Create the input labels and entry fields
label1 = tk.Label(window, text="Enter the first number:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Enter the second number:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

# Create the button to calculate the sum
calculate_button = tk.Button(window, text="Calculate", command=calculate_sum)
calculate_button.pack()

# Create the label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()
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

def reverse_word():
    word = entry.get()
    reversed_word = word[::-1]
    result_label.config(text=f"Reversed word: {reversed_word}")

# Create the main window
window = tk.Tk()
window.title("Word Reverser")

# Create the input label and entry field
label = tk.Label(window, text="Enter a word:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create the button to reverse the word
reverse_button = tk.Button(window, text="Reverse", command=reverse_word)
reverse_button.pack()

# Create the label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()
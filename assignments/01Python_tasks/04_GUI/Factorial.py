import tkinter as tk
import math

def calculate_factorial():
    try:
        num = int(entry.get())
        result = math.factorial(num)
        result_label.config(text=f"Factorial: {result}")
    except ValueError:
        result_label.config(text="Invalid input!")

# Create the main window
window = tk.Tk()
window.title("Factorial Calculator")

# Create the input label and entry field
label = tk.Label(window, text="Enter an integer:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create the button to calculate the factorial
calculate_button = tk.Button(window, text="Calculate", command=calculate_factorial)
calculate_button.pack()

# Create the label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()
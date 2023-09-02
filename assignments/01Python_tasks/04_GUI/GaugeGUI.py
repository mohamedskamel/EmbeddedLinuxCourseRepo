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

def update_gauge(value):
    angle = (value - min_value) * (max_angle - min_angle) / (max_value - min_value) + min_angle
    canvas.itemconfigure(needle, angle=angle)

# Configuration
min_value = 0
max_value = 100
min_angle = -150
max_angle = 150

# Create the main window
window = tk.Tk()
window.title("Car Gauge")

# Create a canvas to draw the gauge
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Draw the gauge background
canvas.create_arc(50, 50, 350, 350, start=min_angle, extent=max_angle-min_angle, style=tk.ARC, width=10)

# Draw the needle
needle = canvas.create_line(200, 200, 200, 50, width=5)

# Create a scale
scale = tk.Scale(window, from_=min_value, to=max_value, orient=tk.HORIZONTAL, command=update_gauge)
scale.pack()

# Start the Tkinter event loop
window.mainloop()
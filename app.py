import tkinter as tk
from tkinter import colorchooser

# Create the main application window
root = tk.Tk()
root.title("Color Changing Rectangle")

# Create a Canvas widget to draw on
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Draw a rectangle with a default color
rectangle = canvas.create_rectangle(50, 50, 150, 150, fill="blue")

# Function to change the color of the rectangle
def change_color():
    color = colorchooser.askcolor(title="Choose a color")
    if color[1] is not None:
        canvas.itemconfig(rectangle, fill=color[1])

# Button to change the color when clicked
color_button = tk.Button(root, text="Change Color", command=change_color)
color_button.pack()

# Run the application
root.mainloop()

#!/usr/bin/python3
"""Create a Tkinter application that displays
two labels – One saying “Hello”
and the other saying “World!”.

These should be stacked vertically
on top of each other so the
“Hello” label is above the “World!” label."""
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World")
root.option_add("*Font", "Arial 20")

# Create the labels
hello_label = tk.Label(root, text="Hello")
world_label = tk.Label(root, text="World!")

# Arrange the labels vertically
hello_label.pack(side=tk.TOP, padx=40, pady=20)
world_label.pack(side=tk.TOP, padx=40, pady=20)

# Run the application
root.mainloop()

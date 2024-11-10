#!/usr/bin/python3
"""Create a Tkinter application that contains two labels,
a text entry widget, and two buttons.

The first label should say “Enter your name:”,
the text entry widget should allow the user to enter a name,
and the final label should say “Hello {name}” where {name}
is the input provided in the text box. The two buttons
should be labelled as “Submit” and “Clear”

Write code so that when the “Submit” button is pressed,
the value present in the name text entry widget is used
to populate the “Hello {name}” label. Configure the “Clear”
button so that when it is pressed, the text in the
name text entry widget is cleared, and the “Hello {name}”
label is updated to no longer display a name."""
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Greeting App")
root.option_add("*Font", "Arial 20")

# Labels
name_label = tk.Label(root, text="Enter your name:")
greeting_label = tk.Label(root, text="")

# Text Entry Widget
name_entry = tk.Entry(root, width=30, justify="center")

# Buttons
submit_button = tk.Button(root, text="Submit")
clear_button = tk.Button(root, text="Clear")


def submit_name():
    """Set name"""
    name = name_entry.get()
    greeting_label.config(text=f"Hello {name}")


def clear_fields():
    """Clear name"""
    name_entry.delete(0, tk.END)
    greeting_label.config(text="")


# Configure buttons
submit_button.config(command=submit_name)
clear_button.config(command=clear_fields)

# Layout widgets
name_label.pack_configure(pady=20)
name_entry.pack_configure(padx=50)
submit_button.pack_configure(side=tk.LEFT, padx=50)
clear_button.pack_configure(side=tk.RIGHT, padx=50)
greeting_label.pack_configure(pady=50)

# Run the application
root.mainloop()

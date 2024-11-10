#!/usr/bin/python3
"""Create a Tkinter application that allows
a user to add one to, subtract one from, or double a value.

The application should use a grid layout setup like so:
Row 1 - Three buttons, evenly sized, “Add one”, “Subtract one”, and “Double”
Row 2 - A Label which displays the value
Row 3 - A button centre aligned and one third of the UI width called “Reset”

Application requirements:
The value label should initially start with a value of 0.
When the “Add one” button is pressed, the value of the value label should be incremented by 1.
When the “Subtract one” button is pressed, the value of value label should be decremented by 1
When the “Double” button is pressed, the value of value label should be doubled.
When the “Reset” button is pressed, the value of value label should be set back to 0"""
import tkinter as tk


class ValueModifierApp:
    """Value Modifier"""

    def __init__(self):
        self.root = root
        self.value = 0

        # Create widgets
        self.create_widgets()

        # Arrange widgets using grid layout
        self.arrange_widgets()

        # Initial value
        self.update_display_label()

    def create_widgets(self):
        """Create"""
        self.add_button = tk.Button(
            self.root, text="Add one", command=self.add_one, width=15
        )
        self.subtract_button = tk.Button(
            self.root, text="Subtract one", command=self.subtract_one, width=15
        )
        self.double_button = tk.Button(
            self.root, text="Double", command=self.double_value, width=15
        )

        # Centered input field (using Entry instead of Label)
        self.display_label = tk.Label(
            self.root, width=20, justify="center", font=("Helvetica", 24)
        )

        self.reset_button = tk.Button(
            self.root, text="Reset", command=self.reset_value, width=15
        )

    def arrange_widgets(self):
        """Arrangement"""
        self.add_button.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.subtract_button.grid(
            row=0, column=1, sticky="nsew", padx=20, pady=20
        )
        self.double_button.grid(
            row=0, column=2, sticky="nsew", padx=20, pady=20
        )

        self.display_label.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.reset_button.grid(row=2, column=1, sticky="ew", padx=20, pady=20)

        # Make columns expandable
        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1)

        # Make rows expandable except for the last one
        for i in range(2):
            self.root.grid_rowconfigure(i, weight=1)

    def add_one(self):
        """+1"""
        self.value += 1
        self.update_display_label()

    def subtract_one(self):
        """-1"""
        self.value -= 1
        self.update_display_label()

    def double_value(self):
        """x2"""
        self.value *= 2
        self.update_display_label()

    def reset_value(self):
        """=0"""
        self.value = 0
        self.update_display_label()

    def update_display_label(self):
        """Update"""
        self.display_label.config(text=str(self.value))


# Create the main window
root = tk.Tk()
root.title("Value Modifier")
root.option_add("*Font", "Arial 20")


# Create and run the application
app = ValueModifierApp()
root.mainloop()

#!/usr/bin/python3
"""Create a flask application for saying hello 
to a person in random ways. The application 
should always show a text input for a user to 
input a name, and a button labelled 'Submit'.

When the submit button is pressed, the 
application displays a salutation to the 
provided name. The salutation should be 
randomly picked from the following list:
Hello
Hi
G'day
Greetings
As an example, when a user types in “Carla” 
into the text box and presses the submit button, 
the application could display “Greetings Carla”. 
If the user presses the button again, the application 
could display “Hi Carla”, or any of the other 
salutations including the already displayed salutation."""
import html
import random
from flask import Flask, render_template_string

app = Flask(__name__)
words = ["Hello", "Hi", "G'day", "Greetings"]


@app.route("/person/<first_name>")
def person_page(first_name):
    """Simple message"""
    return render_template_string(
        f"<h1>{random.choice(words)} {html.escape(first_name)}</h1>"
    )


if __name__ == "__main__":
    app.run(debug=True)

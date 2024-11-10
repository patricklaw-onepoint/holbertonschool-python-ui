#!/usr/bin/python3
"""Create a flask application that makes use of a 
rendering template to wish a user hello and tell 
them the current date in Brisbane Australia.

Similar to the HTML Escaping task, the application 
should make use of a variable under a route “/person/” 
that should provide the name for a person. That name 
should then be used along with a rendering template 
to display “Hello {name}, today’s date is 
{date in Brisbane yyyy-mm-dd}.” The text should be H1 sized.

As an example, when passed “/person/James” and 
if the current date in Brisbane is the 12th of 
June 2024, the webpage would display “Hello James, 
today’s date is 2024-06-12."""
from flask import Flask, render_template_string
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route("/person/<name>")
def greet_person(name):
    """Greeting"""
    brisbane_tz = pytz.timezone("Australia/Brisbane")
    current_date = datetime.now(brisbane_tz).strftime("%Y-%m-%d")

    rendered_html = render_template_string(
        f"<h1>Hello {name}, today's date is {current_date}.</h1>"
    )

    return rendered_html


if __name__ == "__main__":
    app.run(debug=True)

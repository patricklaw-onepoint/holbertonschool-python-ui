#!/usr/bin/python3
"""Create a gradio application that contains 
a text input field called object, a slider that 
has values between 1 and 10, a text output field, 
and a button called submit.

When a user types a word into the object field, 
and presses the submit button, the output should 
display the word in the output field the number 
of times specified in the slider seperated by a space.

For example, if a user typed ;l'Car' into the 
object text field input, set the slider to 4, 
and pressed submit, the output field should 
display 'Car Car Car Car'. If a user typed 'Bus'
into the object text field input, set the slider to 1, 
and pressed submit, the output field should display 'Bus'."""
import gradio as gr


def result(text, slider):
    """Generate the output"""
    return " ".join([text] * slider)


# Create the interface
app = gr.Interface(
    fn=result,
    inputs=[
        gr.Textbox(label="Object"),
        gr.Slider(
            minimum=1, maximum=10, step=1, label="Number of occurrences"
        ),
    ],
    outputs=gr.Textbox(label="Output"),
    title="Text Repeater",
    description="Type a word in the Object field and adjust the slider to specify the number of occurrences.",
)

if __name__ == "__main__":
    app.launch()

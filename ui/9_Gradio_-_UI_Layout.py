#!/usr/bin/python3
"""Create a gradio application that makes 
use of a block layout. The application 
should be made up of three rows, 
each holding different components.

The first row should contain a markdown component, 
that displays the text “Python code scratch pad”. 
The text should be in the markdown single # style.

The second row should contain a code component, 
set to use python as the language and displaying 
the code snippet print('Hello World!'). 
The code component should be configured 
to allow a user to edit the code within it.

The final row should contain two buttons next to 
each other 'Reset' and 'Clear'. When the 
clear button is pressed, the code box should be 
emptied, and when the reset button is pressed, 
the code box should return to it's original 
state displaying print('Hello World!')."""
import gradio as gr

with gr.Blocks() as app:
    # First row: Markdown component
    gr.Markdown("# Python code scratch pad")

    # Second row: Code component
    code = gr.Code(
        label="Code",
        value="print('Hello World!')",
        lines=5,
        max_lines=5,
        language="python",
        interactive=True,
    )

    # Third row: Buttons
    with gr.Row():
        gr.Button("Reset").click(
            lambda x: "print('Hello World!')", outputs=code
        )
        gr.Button("Clear").click(lambda x: "", outputs=code)

if __name__ == "__main__":
    app.launch()

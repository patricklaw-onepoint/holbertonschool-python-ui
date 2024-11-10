#!/usr/bin/python3
"""Create a Gradio application that 
displays the words “Hello Markdown World!”

The application should make use of a single 
gradio markdown component, and the text 
should use the Markdown single # header size."""
import gradio as gr

with gr.Blocks() as app:
    gr.Markdown("# Hello Markdown World!")

if __name__ == "__main__":
    app.launch()

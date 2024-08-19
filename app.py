import gradio as gr

def fn(input):
    return input

gr.Interface(fn, ['text'], ['text']).launch()

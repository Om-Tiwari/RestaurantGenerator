from fastapi import FastAPI
import gradio as gr
from langchainhelper import generate_restaurant

app = FastAPI()

# Create a Gradio interface
interface = gr.Interface(
    fn=generate_restaurant,
    inputs=gr.Textbox(label="Country"),
    outputs=[
        gr.Markdown(label="Restaurant Name"),
        gr.Markdown(label="Menu Items"),
    ],
    title="Restaurant Generator",
)


app = gr.mount_gradio_app(app, interface, path="/")
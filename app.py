import gradio as gr
from langchainhelper import generate_restaurant

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



# Launch the interface
interface.launch(share="True")

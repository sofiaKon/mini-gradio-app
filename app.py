import gradio as gr
import spaces


@spaces.GPU
def predict(name):
    name = name.strip()

    if not name:
        return "Please enter your name."

    return f"Hello, {name}! Welcome to my Gradio app 🚀"


demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(label="Type your name"),
    outputs=gr.Textbox(label="Greeting"),
    title="My Mini Gradio App",
    description="A simple Gradio application deployed with GitHub Actions.",
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)

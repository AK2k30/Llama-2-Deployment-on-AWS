import gradio as gr
import requests

API_URL = "https://y2tf7fxa3m.execute-api.eu-north-1.amazonaws.com/LLama-2"

def chatbot(message):
    # Construct the API URL with the user's query
    full_url = f"{API_URL}?query={message}"
    
    try:
        # Send a GET request to the API
        response = requests.get(full_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Return the text response directly
        return response.text
    except requests.RequestException as e:
        return f"An error occurred: {str(e)}"

# Create the Gradio interface
iface = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(lines=2, placeholder="Enter your message here..."),
    outputs="text",
    title="AI Chatbot",
    description="Enter your message, and the AI will respond.",
    theme="default",
    examples=[
        ["What is the capital of France?"],
        ["Tell me a joke about programming."],
        ["Explain quantum computing in simple terms."]
    ]
)

# Launch the Gradio app
iface.launch()
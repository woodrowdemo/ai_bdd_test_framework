from openai import OpenAI #Importing OpenAI class from openai module
from config.prompts import prompts #Importing prompts dictionary directly
import json

# Initialize OpenAI API client with the API key
def initialize_client():
    with open("config/openai_key.json", "r") as f:
        api_key = json.load(f)["api_key"]
    return OpenAI(api_key=api_key)

client = initialize_client() #Creating an instance of OpenAI class with the API key

def load_prompt(key):
    """Retrieve a prompt from the prompts dictionary."""
    return prompts.get(key, "Prompt not found.")

#Generate text using OpenAI
def generate_text(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", #Specifying the model to use
        messages=messages, #Specifying the messages to send
        max_tokens=700, #Specifying the maximum number of tokens to generate to minimize cost
    )

    return response.choices[0].message.content.strip() #Returning the generated text
    
    
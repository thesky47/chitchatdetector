import openai
import os 
from dotenv import load_dotenv

def categorize_sentence(sentence):
    prompt = f"Please categorize the following sentence as chitchat or not chitchat: '{sentence}'."
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose different engines based on your needs
        prompt=prompt,
        temperature=0,
        max_tokens=20
    )
    
    return response

openai.api_key = os.getenv("OPENAI_API_KEY")

print(categorize_sentence(input("enter text: ")))

import streamlit as st
import os 
import pickle
from dotenv import load_dotenv
from streamlit_extras.add_vertical_space import add_vertical_space
import openai

# Sidebar contents
with st.sidebar:
    st.title('ChitChat Detector ')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
    ''')
    add_vertical_space(5)
    st.write('Made by Akash Bindu')

def categorize_sentence(sentence):
    prompt = f"As Language Expert, Categorize the following sentence as chitchat or not chitchat. If the provided sentence is chitchat, respond with 'It’s chitchat'. If it's not chitchat, respond with 'It’s not chitchat'. Also, provide a confidence score for your answer, confidence score should be a value between 0 and 1: '{sentence}'."
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose different engines based on your needs
        prompt=prompt,
        temperature=0,
        max_tokens=20
    )
    
    return response.choices[0].text.strip()

def main():
    load_dotenv()
    st.header("Chit Chat Detector")

    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    #os.environ['OPENAI_API_KEY'] = st.text_input("OpenAI API Key:", type="password")

    if query := st.text_input("Enter a Sentence: "):
        st.write(categorize_sentence(query))


if __name__ == '__main__':
    main()
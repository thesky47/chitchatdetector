import openai

def categorize_sentence(sentence):
    prompt = f"Please categorize the following sentence as chitchat or not chitchat: '{sentence}'."
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose different engines based on your needs
        prompt=prompt,
        temperature=0,
        max_tokens=20
    )
    
    return response

openai.api_key = "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"

print(categorize_sentence(input("enter text: ")))

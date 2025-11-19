import openai

openai.api_key = "YOUR_API_KEY_HERE"

def ask_ai(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful study AI for school students."},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']

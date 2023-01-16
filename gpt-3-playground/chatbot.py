import openai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')


def ask(input_question):
    output = openai.Completion.create(
        model='text-davinci-003',   # these are the different models: https://beta.openai.com/docs/models/gpt-3
        prompt=input_question,
        max_tokens=100,     # controls how long the answer is
        temperature=0.7,    # controls how create the answer is
        api_key=API_KEY
    )
    ai_answer = output.choices[0].text
    return ai_answer


if __name__ == '__main__':
    print("Eyo, what's good?")

    while (question := input('\n> ')) != 'EXIT':
        answer = ask(question)
        print(answer)
import openai
import os
from dotenv import load_dotenv
import nltk

load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')

# Here are the different models: https://beta.openai.com/docs/models/gpt-3
models = ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"]

reference_text = "The quick brown fox jumps over the lazy dog."


def ask(input_question):
    response = openai.Completion.create(
        model=models[0],
        prompt=input_question,
        max_tokens=100,  # controls how long the answer is
        temperature=0.5,  # controls how create the answer is
        api_key=API_KEY
    )
    ai_answer = response.choices[0].text
    return ai_answer


def performance_evaluation(input_question):
    generated_texts = {}
    for model in models:
        response = openai.Completion.create(
            model=model,
            prompt=input_question,
            max_tokens=100,
            temperature=0.5,
            api_key=API_KEY
        )
        generated_texts[model] = response["choices"][0]["text"]

    # Compare the generated text to the reference text using the BLEU score
    results = []
    for model, generated_text in generated_texts.items():
        bleu_score = nltk.translate.bleu_score.sentence_bleu([input_question], generated_text)
        results.append(f"{model} BLEU score: {bleu_score}")
    return results


if __name__ == '__main__':
    print("Eyo, what's good?")

    while (question := input('\n> ')) != 'EXIT':
        if question == 'Performance evaluation':
            prompt = input("Performance evaluation requested! Please enter a prompt based on which the models will be compared:\n")
            results = performance_evaluation(prompt)
            for result in results:
                print(result)
        else:
            answer = ask(question)
            print(answer)

# BabyGPT - a simple project for me to play around with OpenAI's API
## Prerequisites
 - At least Python 3.8
 - OpenAI API key - you can generate one, by [creating an account](https://openai.com/api/), then navigating to Personal > View API key > Create new secret key, then save the API key to a file named ```.env``` in a variable called ```OPENAI_API_KEY```
 - ```pip install openai``` - installs the OpenAI library
 - ```pip install python-dotenv``` - allows the application to fetch environmental variables from a .env file

## Language models performance evaluation
In their [documentation](https://beta.openai.com/docs/models/gpt-3), OpenAI advertise ```text-davinci-003``` as the most capable language model and ```text-ada-001``` as the fastest one. I wanted to see how this translates into numbers, so I used the [Natural Language Toolkit (nltk)](https://www.nltk.org/) to get the [BLEU](https://en.wikipedia.org/wiki/BLEU) score of each language model.

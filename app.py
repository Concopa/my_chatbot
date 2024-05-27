"""
My OpenAI chatbot. Testing to see if it will be cheaper monthly than ChatGPT
Practice with programming in Python

Current API Price (May 27, 2024)
Model gpt-4o
Input
$5.00 / 1M tokens

Output
$15.00 / 1M tokens
"""
from openai import OpenAI
import keys

MODEL = "gpt-4o"

"""
Secret keys for OpenAI stored in keys.py
https://platform.openai.com/settings/profile
Format:
organization = 'key'
project = 'key'
api_key = 'key'
"""

client = OpenAI(
    organization=keys.organization,
    project=keys.project,
    api_key=keys.api_key,
)

# Printing output so I remember what is going on with sample code
print(f"You are a helpful assistant. Help me with programming python questions!")
print(f"What is a class in python?")

# Example from https://cookbook.openai.com/examples/gpt4o/introduction_to_gpt4o
completion = client.chat.completions.create(
    model=MODEL,
    messages=[
        # This is the system message that provides context to the model
        {"role": "system", "content": "You are a helpful assistant. Help me with programming python questions!"},
        # This is the user message for which the model will generate a response
        {"role": "user", "content": "What is a class in python?"}
    ],
    temperature=1,
    max_tokens=512,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print("Assistant: " + completion.choices[0].message.content)

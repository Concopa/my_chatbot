"""
My OpenAI chat bot. Testing to see if it will be cheaper monthly than ChatGPT
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


"""
Secret keys for OpenAI stored in keys.py
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

client.models.list()

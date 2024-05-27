"""
My OpenAI chat bot. Testing to see if it will be cheaper monthly than ChatGPT
Practice with programming in Python
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

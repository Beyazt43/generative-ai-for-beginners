import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["GITHUB_TOKEN"],
    base_url="https://models.inference.ai.azure.com",
)

model = "gpt-4.1-mini"

prompt = "Complete the following story: Once upon a time there was a girl who peacefully lived on a remote space colony but one day"

response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "system",  # role = who is speaking, system = the AI, user = you
            "content": "You continue stories exactly where they end. Never rewrite or restart them.",  # content = what they said, system = instructions for the AI, user = your prompt
        },
        {
            "role": "user",
            "content": "Once upon a time there was a girl who peacefully lived on a remote space colony, but one day",
        },
    ],
)

print(response.choices[0].message.content)

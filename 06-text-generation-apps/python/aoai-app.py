import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["GITHUB_TOKEN"],
    base_url="https://models.inference.ai.azure.com",
)

model = "gpt-4.1-mini"

prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model=model,
    input=prompt,
)

print(response.output_text)

# pylint: disable=all
import os

from dotenv import load_dotenv
from openai import OpenAI

# load environment variables from .env file
load_dotenv()

# configure the OpenAI client against the Azure OpenAI (Microsoft Foundry) v1 endpoint
client = OpenAI(
    api_key=os.environ["GITHUB_TOKEN"],
    base_url="https://models.inference.ai.azure.com",
)

model = "gpt-4.1-mini"

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
# make a request using the Responses API
response = client.responses.create(
    model=model,
    input=prompt,
)

# print response
print(response.output_text)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
# test

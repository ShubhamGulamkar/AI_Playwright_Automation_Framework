import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a Playwright automation expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content


# import openai
# import os

# openai.api_key = os.getenv("OPENAI_API_KEY")

# def ask_llm(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a Playwright automation expert."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0
#     )
#     return response.choices[0].message["content"]

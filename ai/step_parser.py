import json
from ai.llm_client import ask_llm

def parse_steps(steps_text: str):
    prompt = f"""
You are an automation engine.

STRICT RULES:
- Return ONLY valid JSON
- Do NOT add explanations
- Do NOT use markdown
- Do NOT use backticks
- Do NOT add comments

JSON FORMAT:
[
  {{
    "action": "goto",
    "url": "LOGIN_URL"
  }},
  {{
    "action": "fill",
    "role": "textbox",
    "name": "Username",
    "value": "tomsmith"
  }}
]

Convert the following test steps into JSON actions:

{steps_text}
"""

    response = ask_llm(prompt)
    return json.loads(response)


# import json
# from ai.llm_client import ask_llm

# def parse_steps(natural_language_steps):
#     prompt = f"""
# Convert the following test steps into Playwright actions in JSON.

# Steps:
# {natural_language_steps}

# Output format:
# [
#   {{ "action": "goto", "value": "url" }},
#   {{ "action": "fill", "field": "Username", "value": "admin" }},
#   {{ "action": "click", "role": "button", "name": "Login" }}
# ]
# """
#     response = ask_llm(prompt)
#     return json.loads(response)

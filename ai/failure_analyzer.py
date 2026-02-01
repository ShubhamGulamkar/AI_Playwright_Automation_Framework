from ai.llm_client import ask_llm

def analyze_failure(error, steps):
    prompt = f"""
Test failed with error:
{error}

Executed steps:
{steps}

Explain the root cause and suggest a fix.
"""
    return ask_llm(prompt)

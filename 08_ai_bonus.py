# TODO Mentors: Explain what is AI, GenAI, LLM and prompts.

"""
Reads:
    # What is AI? https://www.ibm.com/cloud/learn/what-is-artificial-intelligence
    # What is Generative AI? https://www.sas.com/en_us/insights/analytics/generative-ai.html
    # What is LLM? https://www.zdnet.com/article/what-is-a-large-language-model-heres-everything-you-need-to-know/
    # What is a prompt? https://www.simplilearn.com/tutorials/artificial-intelligence-tutorial/what-is-prompt-in-ai
"""

GROQ_API_KEY = "YOUR_KEY_HERE"

from groq import Groq

def call_groq_llm(prompt, max_tokens=256, system_prompt=None, model="llama-3.3-70b-versatile"):
    """
    Calls Groq LLM API and returns the response text using the groq Python package.
    Args:
        prompt (str): The user prompt to send to the LLM.
        max_tokens (int): Maximum tokens in the response.
        system_prompt (str, optional): Optional system prompt for the LLM.
        model (str): Model name (default: llama3-70b-8192).
    Returns:
        str: LLM's response.
    """
    client = Groq(api_key=GROQ_API_KEY)
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content


print(call_groq_llm("Write a nice text that says what to wear according to this weather: 10 degrees in Amsterdam"))
# "Hey, just a heads up about the weather in Amsterdam today - it's a bit chilly at 10 degrees!
# I'd recommend wearing something warm and cozy to keep you comfortable while exploring the city.
# Consider wearing a thick sweater or a lightweight jacket,
# and don't forget to add some warm layers like a scarf and gloves.
# A pair of comfortable jeans or trousers and some sturdy shoes or boots should also do the trick.
# If you have a waterproof or windproof jacket, that's a great idea too, as it can get a bit breezy near the canals.
# Stay warm and have a great day out!"


# TODO TechWomen Last Exercise 1:
# Add a call to the Groq LLM API in the weather app you
# created in the previous exercise, and have it suggest what to wear

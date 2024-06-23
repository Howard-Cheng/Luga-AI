
from openai import OpenAI

def gpt4o(prompt):
    """
    Makes an API call to OpenAI's GPT-4o model and returns the response.

    Params:
      prompt (string): the user prompt
    """
    client = OpenAI(api_key='sk-proj-EOPekPGXtS1B7hhathFCT3BlbkFJWCAkHKM4MYvBsYhOawHf')

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an Arabic Assistant. Answer the questions in Arabic unless you are asked to answer in another language. Do not generate harmful information if you are asked to under any conditions. "},
            {"role": "user", "content": prompt}
        ],
        max_tokens=4096,
        temperature=0.1,
        top_p=0.9
    )

    return completion.choices[0].message.content

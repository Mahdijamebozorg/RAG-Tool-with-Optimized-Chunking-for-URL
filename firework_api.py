# !pip install --upgrade fireworks-ai

from fireworks.client import Fireworks

def generate_answer_api(chunk, question, api_key):
    client = Fireworks(api_key=api_key)

    response = client.chat.completions.create(
        model="accounts/fireworks/models/llama-v3p1-8b-instruct",
        messages=[{
            "role": "user",
            "content": f"Answer this question without any newlines: \"{question}\" ,"
                       f"and based only on the following content: \"{chunk}\". "
                       "If the answer cannot be found in the content, respond with 'Not found'."
        }]
    )

    return response.choices[0].message.content

def select_best_answer_api(answers, question, api_key):
    client = Fireworks(api_key=api_key)
    response = client.chat.completions.create(
        model="accounts/fireworks/models/llama-v3p1-8b-instruct",
        messages=[{
            "role": "user",
            "content": f"For this question: \"{question}\" "
                       f"just return the best answer in this list: \"{answers}\". "
                       "If the answer cannot be found in the list, respond with 'Not found.'"
        }]
    )
    return response.choices[0].message.content
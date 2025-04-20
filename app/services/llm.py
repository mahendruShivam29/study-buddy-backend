import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_questions_and_flashcards(content: str):
    prompt = f"""
    Based on the following study material:
    {content}

    Generate:
    - 5 multiple choice questions with answers
    - 5 flashcards (term:definition)
    Return in JSON format.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

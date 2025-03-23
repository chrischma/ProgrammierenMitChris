
from openai import OpenAI
from dotenv import load_dotenv
from os import getenv


load_dotenv()
API_KEY = getenv("API_KEY")


def get_gpt_answer(prompt):                
    client = OpenAI(api_key=API_KEY)
    prompt = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
            model="gpt-4o-search-preview",
            messages=prompt
    )
    
    text = response.choices[0].message.content
    return text
   


if __name__ == "__main__":
    res = get_gpt_answer("Wie heißt der aktuelle Bürgermeister von Zürich?")
    print(res)
    
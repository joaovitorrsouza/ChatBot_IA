from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = ""
client = OpenAI()

def generate_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro na API OpenAI: {str(e)}"

from google import genai
import os
from dotenv import load_dotenv
from src.prompt import system_instruction
from google.genai import types

load_dotenv()

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


client = genai.Client(api_key=GOOGLE_API_KEY)


def ask_order(message,model="gemini-1.5-pro"):
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction=system_instruction),
    contents=message)

    return response.text


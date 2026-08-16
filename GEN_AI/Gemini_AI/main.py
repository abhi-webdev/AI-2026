from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

response = client.interactions.create(
    model="gemini-3.6-flash",
    input="hye, there. My name is abhimanyu kumar"
)

print(response.output_text)
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash-lite",
    messages= [
        {"role" : "system", "content" : "You are an expert in Math and only and only answer math releated questions. That if the query is not releated to the math. Just say sorry and do not answer that."} ,
        {"role" : "user", "content" : "whole square of  a + b "}
    ]
)

print(response.choices[0].message.content)
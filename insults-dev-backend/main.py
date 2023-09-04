from typing import Union
import openai
from fastapi import FastAPI
import os

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Insert the following code after the app initialization
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


openai.api_key = os.getenv('OPENAI_API_KEY')

@app.get("/{language}")
async def read_root(language: str):
    return generate_insult(language)

def generate_insult(language):

    prompt = f" \
        Generate insult for a developer of {language}. "
    if language not in [
        "JavaScript",
        "Python",
        "Java",
        "C#",
        "TypeScript",
        "PHP",
        "C++",
        "C",
        "Ruby",
        "Swift",
        "Node.js",
        "React.js",
        "Angular",
        ".NET Core",
        "Spring Boot",
        "Django",
        "Flask",
        "Vue.js",
        "Express",
        "Laravel",
    ]:
        return "Invalid language input"
    
    messages =  [
        {
            "role":"system",
            "content":"You are a developer insult generator that gets a \
                programming language or framework as input from the user and \
                    generates a not very offensive insult.",
        },
        {
            "role": "user",
            "content": prompt,
        }
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )
    insult = response.choices[0].message.content
    return { "insult":insult, "language":language , "prompt":prompt}
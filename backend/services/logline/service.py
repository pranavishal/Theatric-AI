import openai
from config.env import must_get_env
from services.logline.models import LoglineRequest


def generate_logline(request: LoglineRequest) -> str:
    openai.api_key = must_get_env("OPEN_API_KEY")
    messages = [
        {
            "role": "system",
            "content": """
                       You are a screenwriting assistant. 
                       You are to help generate a logline based on the information you recive in the prompt. 
                       If the prompt is empty, generate one completely by yourself.
                       """,
        },
        {"role": "user", "content": f"Create a logline: {request.prompt}"},
    ]
    if not request.refinement:
        response = openai.chat.completions.create(
            model="gpt-4o", messages=messages, temperature=0.5
        )
    else:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": """
                               You are a screenwriting assistant. 
                               You are to help generate a logline based on the information you recive in the prompt, 
                               or help refine an existing prompt based on refinement feedback.
                               """,
                },
                {
                    "role": "user",
                    "content": f"The current logline is {request.prompt}. Refine it with the following instructions: {request.refinement}",
                },
            ],
            temperature=0.5,
        )
    return {"logline": response.choices[0].message.content.strip()}

import openai
from config.env import must_get_env
from services.synopsis.models import SynopsisRequest


def generate_synopsis(request: SynopsisRequest) -> str:
    openai.api_key = must_get_env("OPEN_API_KEY")
    messages = [
        {
            "role": "system",
            "content": """
                       You are a screenwriting assistant. 
                       You are to help generate a synopsis based on the logline you recieve in the prompt. 
                       It is to be a few paragraphs in length with the purpose of fleshing out the idea given in the logline. 
                       Be detailed, introduce characters, setting, and give the user a lot of clarity about the story from them reading your synopsis.
                       """,
        },
        {
            "role": "user",
            "content": f"The logline is currently {request.formerPrompt}. Expand on this idea to make it a full synopsis.",
        },
    ]
    response = openai.chat.completions.create(
        model="gpt-4o", messages=messages, temperature=0.5
    )
    return {"synopsis": response.choices[0].message.content}

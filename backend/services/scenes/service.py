import openai
from config.env import must_get_env
from services.scenes.models import SceneRequest

def generate_scenes(request: SceneRequest) -> str:
    openai.api_key = must_get_env("OPENAI_API_KEY")
    messages = [
        {
            "role": "system",
            "content": """
                       You are a film editor helping break down a movie synopsis into a series of cinematic visual scenes for a trailer.

                        Your job is to extract 6 unique, visually rich scenes from the synopsis. Focus on setting and mood, not dialogue or specific character actions.

                        Each scene should be described as a film shot — atmospheric, visual, and short (5–12 seconds in duration).

                        Return the result as a JSON list. Each object must include:
                        - scene_id (1–6)
                        - summary (1–2 sentences describing the visual shot, avoiding character detail)
                        - tone (e.g. eerie, romantic, tense)
                        - duration (recommended number of seconds, between 5–12)

                       """,
        },
        {
            "role": "user",
            "content": f"The synopsis: {request.synopsis}.",
        },
    ]
    response = openai.chat.completions.create(
        model="gpt-4o", messages=messages, temperature=0.5
    )
    return response.choices[0].message.content
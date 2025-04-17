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

                        Each scene should be described as a film shot — atmospheric, visual, and short (5–12 seconds in duration). These will be sent to SORA or another video generator, so make sure you give enough detail.

                        Also, do remember: THIS IS A TRAILER! Each scene shouldn't just be a chronological retelling of the synopsis. We don't just want to give away the flow of events.
                        Instead, think of the most visually striking moments that would entice an audience to watch the film. Don't give away vital ingformation or the ending.
                        The scenes should be visually distinct and create a sense of anticipation, excitement, or intrigue.


                        Return the result as a JSON list. Each object must include:
                        - scene_id (1–6)
                        - summary (1–2 sentences describing the visual shot, avoiding character detail)
                        - tone (e.g. eerie, romantic, tense)
                        - duration (recommended number of seconds, between 5–12)

                        It is also important to remember that the trailer will have voice narration when created. So when you are giving these scene descriptions, make them
                        something that can easily be described or be talked about with a narrator or monologue voiceover relating to the visuals and story.

                        Please DO NOT FALL INTO THE TRAP OF ALWAYS TRYING TO SHOW A HOPEFUL OR BRIGHT FUTURE AT THE END OF THE TRAILER. MIX IT UP.
                        ONLY DO SOMETHING LIKE THAT IF IT FITS THE SYNOPSIS. IF ITS MEANT TO BE DARK, DO NOT MAKE IT LIGHT.

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
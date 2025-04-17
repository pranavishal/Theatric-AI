import openai
from config.env import must_get_env
from services.narration.models import NarrationRequest

def generate_narration(request: NarrationRequest) -> str:
    openai.api_key = must_get_env("OPENAI_API_KEY")
    messages = [
        {
            "role": "system",
            "content": """
                       You are a professional movie trailer narrator writing a unified narration script for a cinematic trailer.
                       You are going to be given a list of six scenes in the trailer. Each scene includes a description, tone, and duration in seconds. It is in JSON format. 
                       Your job is to write one cohesive trailer narration script — one line of narration for each scene — that flows naturally from beginning to end. 
                       The narration should match the tone of each scene and feel like it's spoken by a single omniscient narrator across the whole trailer.
                       You need to keep in mind the duration of the trailer. The narration should be timed to fit within the scene durations, so each line should be short enough to fit within the scene's duration.
                       Rules:
                       - Do NOT mention character names (the narrator is detached from the story)
                       - Use dramatic, mysterious, emotional language — teaser-like, not expositional
                       - The final scene should end with a sense of climax or anticipation, but avoid spoilers
                       - Keep each narration line short enough to fit within its scene's duration (see timing)
                       - Format output clearly: "Scene 1: ..." up to "Scene 6: ..."

                       Please DO NOT FALL INTO THE TRAP OF ALWAYS TRYING TO SHOW A HOPEFUL OR BRIGHT FUTURE AT THE END OF THE TRAILER. MIX IT UP.
                       ONLY DO SOMETHING LIKE THAT IF IT FITS THE SYNOPSIS. IF ITS MEANT TO BE DARK, DO NOT MAKE IT LIGHT.

                       """,
        },
        {
            "role": "user",
            "content": f"The scenes are currently {request.scenes}. Expand on this idea to make it a full narration.",
        },
    ]
    response = openai.chat.completions.create(
        model="gpt-4o", messages=messages, temperature=0.5
    )
    return response.choices[0].message.content
import openai
from config.env import must_get_env
from services.prompts.models import PromptRequest

def generate_prompt(request: PromptRequest) -> str:
    openai.api_key = must_get_env("OPENAI_API_KEY")
    messages = [
        {
            "role": "system",
            "content": """
                       You are a professional prompt engineer. You are responsible for taking in descriptions of scenes for a movie along
                       with their original synopsys. Your task is to then take each scene and generate a very effective prompt that will
                       be given to Google Veo 2 API, which is a video generator, similar to SORA. You are to make sure that each scene gets
                       a very detailed prompt that will help the video generator create a very high quality video. It is also
                       VERY VERY IMPERATIVE THAT ALL PROMPTS ARE MADE SO THAT EACH SCENE IS CONSISTENT WITH EACH OTHER. SO ENSURE YOU
                       ARE CONSISTENT WITH HOW YOU DESCRIBE THE ART STYLE OF EACH SCENE TO THE VIDEO GENERATOR.

                       Your input will be a list of scenes, each with a summary, tone, and duration.
                       Your output should be a list of prompts, one for each scene. Each prompt should include:
                       - scene_id (1–6)
                       - prompt (detailed description for the video generator)
                       - art_style (e.g. realistic, cartoonish, abstract)
                       - duration (recommended number of seconds, between 5–12, which is the same as the scene you are given)
                        - tone (e.g. eerie, romantic, tense)
                        In JSON format, like how you are given your scenes

                        You are also given the original synopsis. You need to make sure that the prompts you are generating
                        are consistent with the original synopsis. 
                       """,
        },
        {
            "role": "user",
            "content": f"The Scenes are: {request.promptBase}. The original synopsis is {request.promptContext}",
        },
    ]
    response = openai.chat.completions.create(
        model="gpt-4o", messages=messages, temperature=0.5
    )

    return response.choices[0].message.content
    
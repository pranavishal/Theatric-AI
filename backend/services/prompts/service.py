import openai
from config.env import must_get_env
from services.prompts.models import PromptRequest

def generate_prompt(request: PromptRequest) -> str:
    openai.api_key = must_get_env("OPENAI_API_KEY")
    
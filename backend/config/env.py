import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def must_get_env(var: str) -> str:
    if var not in os.environ:
        raise KeyError(f"{var} is not an environment variable")

    if os.environ[var] == "":
        raise KeyError(f"{var} environment variable cannot be blank")

    return os.environ[var]

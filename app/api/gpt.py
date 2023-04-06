import openai
from app.utils import logger

def ask_gpt(messages):
    rsp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    logger.info("[gpt] ask rsp=%s", rsp)
    return rsp.get("choices")[0]["message"]["content"]

from flask import Flask
import openai
from dotenv import load_dotenv
import os

# 加载 .env 文件中的配置信息
load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return 'Hi, welcome~'

@app.route("/chat", methods=['POST'])
def chat():
    return 'Hi, dichatgpt!'

if (__name__) == '__main__':
    app.run()

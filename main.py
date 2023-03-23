from flask import Flask
import openai
import os

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

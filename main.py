from flask import Flask
import openai


app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def index():
    return 'Hi, dichatgpt!'

if (__name__) == '__main__':
    app.run()
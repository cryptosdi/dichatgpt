from flask import Flask


app = Flask(__name__)

@app.route("/api/chat")
def index():
    return 'Hi, dichatgpt!'

if (__name__) == '__main__':
    app.run()

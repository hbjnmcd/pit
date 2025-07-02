from flask import Flask
import os

app = Flask(__name__)

pong_response = os.getenv("PONG_RESPONSE", "Pong!")

@app.route('/')
def hello():
    return pong_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
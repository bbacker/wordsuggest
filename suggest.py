# from https://dev.to/apcelent/deploying-flask-on-aws-lambda-4k42
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World!"})

if __name__ == '__main__':
 app.run()

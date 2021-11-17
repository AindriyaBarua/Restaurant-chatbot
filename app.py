from flask import Flask, render_template, request, jsonify

import response_generator

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get')
def get_bot_response():
    message = request.args.get('msg')
    response = ""
    if message:
        response = response_generator.generate_response(message)
        return str(response)
    else:
        return "Missing Data!"


if __name__ == "__main__":
    app.run()

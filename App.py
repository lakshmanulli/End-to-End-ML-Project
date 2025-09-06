from flask import Flask


app = Flask(__name__)

@app.route('/', methods=(['GET', 'POST']))
def index():
    return "we can print a msg here python flask"


if __name__ == '__main__':
    app.run(debug=True)
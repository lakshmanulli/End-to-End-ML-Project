from flask import Flask


app = Flask(__name__)




@app.route('/', methods=(['GET', 'POST']))
def index():

    return "we can print a msg here"


if __name__ == '__main__':
    app.run(debug=True)
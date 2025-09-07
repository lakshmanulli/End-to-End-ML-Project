from flask import Flask
from House_price.logger import logging



app = Flask(__name__)

@app.route('/', methods=(['GET', 'POST']))
def index():
    logging.info("we are in index page")
    return "we can print a msg here python flask"


if __name__ == '__main__':
    app.run(debug=True)
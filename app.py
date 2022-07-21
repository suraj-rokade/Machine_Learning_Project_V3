##first File


import sys
from flask import Flask
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():

    try:
        raise Exception("We are testing Exception")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.errot_message)
        logging.info("We are testing logging module")
    return "CI CD pipline has bee established"

if __name__ == "__main__":
    app.run(debug=True)
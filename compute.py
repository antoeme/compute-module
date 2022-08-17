import json
from flask import Flask,jsonify
import requests
import datetime

from dotenv import load_dotenv
from os import getenv

URL_QUERY = "http://127.0.0.1:5003/query"

# load environment variables from '.env' file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def helloworld():
    return jsonify({"about": " Helloworld !"})

@app.route('/calcoli')
def calcoli():
    row = requests.get(URL_QUERY)
    riga = json.dumps(row.json())
    print(riga)
    return 'presa riga'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=5005)
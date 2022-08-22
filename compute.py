import json
from flask import Flask,jsonify
import requests
import datetime
import math

from dotenv import load_dotenv
from os import getenv

URL_QUERY = "http://127.0.0.1:5003/query"

# load environment variables from '.env' file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def helloworld():
    return jsonify({"about": " Helloworld !"})

@app.route('/calcoli/<int:id>', methods=[ 'GET','POST'])
def calcoli(id):
    row = requests.get(URL_QUERY+'/'+str(id))
    riga = json.dumps(row.json())
    chars = '[]'
    res = riga.translate(str.maketrans('','',chars))
    l = res.split(",")  #formattiamo la stringa levando i caratteri inutili
    a = []
    for i in range(len(l)):
        a.append(float(l[i]))   #trasformiamo gli elementi della lista in float

    minimo = min(a)
    massimo = max (a)

    mean = sum(a) / len(a)
    var = sum((l-mean)**2 for l in a) / len(a)
    st_dev = math.sqrt(var)

    print("Standard deviation of the given list: " + str(st_dev))
    print("media = ", mean)

    print ("min =",minimo)
    print("max = ", massimo)

    dati = {}
    
    
    return 'eseguiti calcoli su elementi'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=5005)
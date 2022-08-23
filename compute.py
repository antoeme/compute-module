import json
from flask import Flask,jsonify
import requests
import datetime
import math

from dotenv import load_dotenv
from os import getenv

NUM_SENSORI = 4
URL_QUERY = "http://127.0.0.1:5003/query"
DATI = []

# load environment variables from '.env' file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def helloworld():
    return jsonify({"about": " Helloworld !"})

@app.route('/calcoli', methods=[ 'GET','POST'])
def calcoli():
    for id in range(NUM_SENSORI):
        row = requests.get(URL_QUERY+'/'+str(id+1))
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
        
        print("Statistiche su sensore: ",id+1)
        print("Standard deviation of the given list: " + str(st_dev))
        print("media = ", mean)

        print ("min =",minimo)
        print("max = ", massimo)

        dati = {"id_sensore":id+1, "min":minimo, "max":massimo, "media":mean, "devs":st_dev }
        DATI.append(dati)
    
    print(DATI)

    
    return 'eseguiti calcoli su elementi'


@app.route('/transfer')
def transfer():
    # if len(DATI) == 0:
    #     return "errore, dati non presenti in memoria"
    # else:
        return (json.dumps(DATI[-1]))   #ritorna l'ultimo dizionario aggiunto

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=5005)
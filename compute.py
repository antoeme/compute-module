import json
import requests
import datetime
import math

from dotenv import load_dotenv
from os import getenv

NUM_SENSORI = getenv("NUM_SENSORI") or 4
URL_QUERY = getenv("URL_QUERY") or "http://127.0.0.1:5003/query"


# load environment variables from '.env' file
load_dotenv()


def calcoli():
    d = []
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
        d.append(dati)
        
    r = requests.post("http://127.0.0.1:5003/statistiche", json = d)
    

    
    return 'eseguiti calcoli su elementi'

calcoli()



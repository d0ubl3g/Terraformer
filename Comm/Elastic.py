import datetime
import json
import logging
import os

from colorama import Style, Fore
from elasticsearch import Elasticsearch

ENV_MAPPING = """{
  "mappings": {
    "properties": {
      "temp":    { "type": "float" },  
      "hum":  { "type": "float"  }, 
      "timestamp":   { "type": "date"  }     
    }
  }
}"""

working_directory = os.path.dirname(os.path.abspath(__file__))


def strToBool(s):
    if s == 'True':
        return True
    elif s == 'False':
        return False
    else:
        return False


with open(working_directory + '/elastic.json') as e:
    data = json.load(e)
    ENDPOINT = data['Endpoint']
    PORT = int(data['Port'])
    TLS = strToBool(data['TLS'])
    USERNAME = data['Username']
    PASSWORD = data['Password']
ENV_INDEX = "env-{}"
EVENT_INDEX = "events-{}"


def initialize():
    try:
        if TLS:
            es = Elasticsearch(
                hosts=ENDPOINT.format(USERNAME, PASSWORD),
                scheme="https",
                port=PORT,
            )
        else:
            es = Elasticsearch(
                hosts=ENDPOINT.format(USERNAME, PASSWORD),
                scheme="http",
                port=PORT,
            )
    except Exception as e:
        es = ""
        print(Style.BRIGHT + Fore.RED + "Error connecting with " + ENDPOINT)
        logging.error(str(e))
    return es


def prepareIndex(index, mapping):
    elastic.create(index=index, body=mapping)


def checkIndexExists(index):
    return elastic.indices.exists(index)


def saveEnv(temp, hum):
    try:
        today = datetime.datetime.today()
        date_index = today.strftime('%d-%m-%Y')
        timestamp = today.isoformat()
        index_name = ENV_INDEX.format(date_index)
        if not checkIndexExists(index_name):
            prepareIndex(index_name, ENV_MAPPING)
        elastic.index(index=index_name, body={"temp": temp, "hum": hum, "timestamp": timestamp})
    except Exception as e:
        logging.error(str(e))


def saveEvent(control, type, msg):
    try:
        today = datetime.datetime.today()
        date_index = today.strftime('%d-%m-%Y')
        timestamp = today.isoformat()
        index_name = EVENT_INDEX.format(date_index)
        elastic.index(index=index_name,
                      body={"control": control, "type": type, "msg": msg, "timestamp": timestamp})
    except Exception as e:
        logging.error(str(e))


elastic = initialize()

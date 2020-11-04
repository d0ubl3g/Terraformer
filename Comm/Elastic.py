import datetime
import json
import logging
import os

from colorama import Style, Fore
from elasticsearch import Elasticsearch

working_directory = os.path.dirname(os.path.abspath(__file__))

with open(working_directory + '/elastic.json') as e:
    data = json.load(e)
    ENDPOINT = data['Endpoint']
    PORT = int(data['Port'])
    TLS = bool(data['TLS'])
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


def saveEnv(temp, hum):
    try:
        today = datetime.datetime.today()
        date_index = today.strftime('%d-%m-%Y')
        timestamp = today.strftime('%d-%m-%Y %H:%M:%S')
        elastic.index(index=ENV_INDEX.format(date_index), body={"temp": temp, "hum": hum, "timestamp": timestamp})
    except Exception as e:
        logging.error(str(e))


def saveEvent(control, type, msg):
    try:
        today = datetime.datetime.today()
        date_index = today.strftime('%d-%m-%Y')
        timestamp = today.strftime('%d-%m-%Y %H:%M:%S')
        elastic.index(index=EVENT_INDEX.format(date_index),
                      body={"control": control, "type": type, "msg": msg, "timestamp": timestamp})
    except Exception as e:
        logging.error(str(e))


elastic = initialize()

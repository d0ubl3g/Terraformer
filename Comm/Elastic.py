import configparser
import datetime
import logging
import os

from colorama import Style, Fore
from elasticsearch import Elasticsearch

working_directory = os.path.dirname(os.path.abspath(__file__))

config = configparser.ConfigParser()
config.read(working_directory + '/elastic.config')

# DEFAULT #
default = config['ELASTIC']
ENDPOINT = default['Endpoint']
PORT = int(default['Port'])
TLS = bool(default['TLS'])
USERNAME = default['Username']
PASSWORD = default['Password']
ENV_INDEX = "env-{}"
EVENT_INDEX = "events-{}"


def initialize():
    try:
        if TLS:
            es = Elasticsearch(
                ENDPOINT,
                http_auth=(USERNAME, PASSWORD),
                scheme="https",
                port=PORT,
            )
        else:
            es = Elasticsearch(
                ENDPOINT,
                http_auth=(USERNAME, PASSWORD),
                scheme="http",
                port=PORT,
            )
    except Exception as e:
        es = ""
        print(Style.BRIGHT + Fore.RED + "Error connecting with " + ENDPOINT)
        logging.error(str(e))
    return es


def saveEnv(temp, hum):
    today = datetime.date.today()
    date_index = today.strftime('%d-%m-%Y')
    elastic.index(index=ENV_INDEX.format(date_index), body={"temp": temp, "hum": hum, "timestamp": today})


def saveEvent(control, type, msg):
    today = datetime.date.today()
    date_index = today.strftime('%d-%m-%Y')
    elastic.index(index=EVENT_INDEX.format(date_index),
                  body={"control": control, "type": type, "msg": msg, "timestamp": today})


elastic = initialize()

import logging

import Adafruit_DHT
import schedule

import Configuration

if Configuration.ELASTIC:
    from Comm import Elastic

import Configuration

TEMP = "0.0"
HUM = "0.0"


def scheduleAuto():
    schedule.every(int(Configuration.ENV_DATA_FREQ)).seconds.do(getTempHum)


def getTempHum():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 15)  # SENSOR , GPIOPIN
    global TEMP
    global HUM
    if humidity is not None and temperature is not None:
        value = "{0:0.1f},{1:0.1f}".format(temperature, humidity)
        TEMP = "{0:0.1f}".format(temperature)
        HUM = "{0:0.1f}".format(humidity)
        logging.debug("Temperature: " + TEMP + "ºC " + "Humidity: " + HUM + "%")
        if Configuration.ELASTIC:
            Elastic.saveEnv(TEMP, HUM)
        return value
    else:
        logging.error("Error receiving data from sensor.")
        return None

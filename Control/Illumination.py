import logging

import schedule

import Configuration
from Comm import RCTransmitter

if Configuration.ELASTIC:
    from Comm import Elastic

ILLU_ON = False


def scheduleHours():
    try:
        schedule.every().day.at(Configuration.ILLU_START_HOUR).do(turnON).tag('illumination-on')
        schedule.every().day.at(Configuration.ILLU_STOP_HOUR).do(turnOFF).tag('illumination-off')
        logging.info("Illumination scheduled: " + Configuration.ILLU_START_HOUR + " to " + Configuration.ILLU_STOP_HOUR)
    except Exception as e:
        logging.error(e)


def turnON():
    try:
        RCTransmitter.sendCommand(RCTransmitter.ILLUMINATION_ON)
        Configuration.DAY = True
        logging.info("Illumination turned on.")
        if Configuration.ELASTIC:
            Elastic.saveEvent("Illumination", "On", "Illumination turned on.")
    except Exception as e:
        logging.error(e)


def turnOFF():
    try:
        RCTransmitter.sendCommand(RCTransmitter.ILLUMINATION_OFF)
        Configuration.DAY = False
        logging.info("Illumination turned off.")
        if Configuration.ELASTIC:
            Elastic.saveEvent("Illumination", "Off", "Illumination turned off.")
    except Exception as e:
        logging.error(e)

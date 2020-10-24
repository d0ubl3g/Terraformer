import logging

import schedule

import Configuration
from Comm import RCTransmitter

ILLU_ON = False


def scheduleHours():
    schedule.every().day.at(Configuration.ILLU_START_HOUR).do(turnON).tag('illumination-on')
    schedule.every().day.at(Configuration.ILLU_STOP_HOUR).do(turnOFF).tag('illumination-off')
    logging.info("Illumination scheduled: " + Configuration.ILLU_START_HOUR + " to " + Configuration.ILLU_STOP_HOUR)


def turnON():
    RCTransmitter.sendCommand(RCTransmitter.ILLUMINATION_ON)
    Configuration.DAY = True
    logging.info("Illumination turned on.")


def turnOFF():
    RCTransmitter.sendCommand(RCTransmitter.ILLUMINATION_OFF)
    Configuration.DAY = False
    logging.info("Illumination turned off.")

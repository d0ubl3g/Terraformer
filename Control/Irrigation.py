import logging
import threading

import schedule

import Configuration
from Comm import RCTransmitter

if Configuration.ELASTIC:
    from Comm import Elastic

IRRIGATION_ON = False
IRRIGATION_IN_CYCLE = False


def scheduleAuto():
    scheduleCycle(Configuration.IRRI_CYCLE_EVERY)
    logging.info("Irrigation cycles scheduled every " + str(Configuration.IRRI_CYCLE_EVERY) + " seconds for " +
                 str(Configuration.IRRI_CYCLE_DURATION) + " seconds.")


def scheduleCycle(e):
    schedule.every(e).seconds.do(cycleON).tag('irrigation-cycle')


def cycleON():
    global IRRIGATION_IN_CYCLE
    IRRIGATION_IN_CYCLE = True
    turnON()
    timer = threading.Timer(float(Configuration.IRRI_CYCLE_DURATION), cycleOFF)
    timer.start()
    logging.info("Irrigation cycle started.")


def cycleOFF():
    global IRRIGATION_IN_CYCLE
    IRRIGATION_IN_CYCLE = False
    turnOFF()
    logging.info("Irrigation cycle finished.")


def turnON():
    global IRRIGATION_ON
    RCTransmitter.sendCommand(RCTransmitter.IRRIGATION_ON)
    IRRIGATION_ON = True
    logging.info("Irrigation turned on.")
    if Configuration.ELASTIC:
        Elastic.saveEvent("Irrigation", "On", "Irrgigation turned on.")


def turnOFF():
    global IRRIGATION_ON
    RCTransmitter.sendCommand(RCTransmitter.IRRIGATION_OFF)
    IRRIGATION_ON = False
    logging.info("Irrigation turned off.")
    if Configuration.ELASTIC:
        Elastic.saveEvent("Irrigation", "Off", "Irrigation turned off.")

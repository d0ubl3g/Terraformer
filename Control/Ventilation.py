import logging

import schedule
import threading

import Configuration
from Comm import RCTransmitter
from Sensors import Receiver

VENTILATION_ON = False
VENTILATION_IN_CYCLE = False


def scheduleAuto():
    schedule.every(int(Configuration.VENT_AUTO_FREQ)).seconds.do(autoAdjust)
    scheduleCycle(int(Configuration.VENT_CYCLE_EVERY), int(Configuration.VENT_CYCLE_DURATION))
    logging.info("Auto Ventilation scheduled every " + Configuration.VENT_AUTO_FREQ + " seconds.")
    logging.info("Ventilation cycles scheduled every " + Configuration.VENT_CYCLE_EVERY + " minutes for " +
                 Configuration.VENT_CYCLE_DURATION + " minutes.")


def scheduleCycle(e, d):
    schedule.every(e).minutes.do(cycleON)


def cycleON():
    global VENTILATION_IN_CYCLE
    VENTILATION_IN_CYCLE = True
    turnON()
    timer = threading.Timer(float(int(Configuration.VENT_CYCLE_DURATION) * 60), cycleOFF)
    timer.start()
    logging.info("Ventilation cycle started.")


def cycleOFF():
    global VENTILATION_IN_CYCLE
    VENTILATION_IN_CYCLE = False
    turnOFF()
    logging.info("Ventilation cycle finished.")


def turnON():
    RCTransmitter.sendCommand(RCTransmitter.VENTILATION_ON)
    logging.info("Ventilation turned on.")


def turnOFF():
    RCTransmitter.sendCommand(RCTransmitter.VENTILATION_OFF)
    logging.info("Ventilation turned off.")


def autoAdjust():
    if Configuration.DAY:
        if Receiver.TEMP >= Configuration.MAX_DAY_TEMP or Receiver.HUM >= Configuration.MAX_DAY_HUM:
            turnON()
        else:
            if not VENTILATION_IN_CYCLE:
                turnOFF()
    else:
        if Receiver.TEMP >= Configuration.MAX_NIGHT_TEMP or Receiver.HUM >= Configuration.MAX_NIGHT_HUM:
            turnON()
        else:
            if not VENTILATION_IN_CYCLE:
                turnOFF()

import logging
import threading

import schedule

import Configuration
from Comm import RCTransmitter
from Sensors import Receiver

EXTRACTION_ON = False
EXTRACTION_IN_CYCLE = False

AUTO_SCHEDULED = True


def scheduleAuto():
    schedule.every(int(Configuration.EXT_AUTO_FREQ)).seconds.do(autoAdjust).tag('extraction-auto')
    scheduleCycle(int(Configuration.EXT_CYCLE_EVERY))
    logging.info("Auto Extraction scheduled every " + Configuration.EXT_AUTO_FREQ + " seconds.")
    logging.info("Extraction cycles scheduled every " + Configuration.EXT_CYCLE_EVERY + " seconds for " +
                 Configuration.EXT_CYCLE_DURATION + " seconds.")

def reScheduleAuto():
    if not AUTO_SCHEDULED:
        schedule.every(int(Configuration.EXT_AUTO_FREQ)).seconds.do(autoAdjust).tag('extraction-auto')


def scheduleCycle(e):
    schedule.every(e).seconds.do(cycleON).tag('extraction-cycle')


def cycleON():
    global EXTRACTION_IN_CYCLE
    EXTRACTION_IN_CYCLE = True
    turnON()
    timer = threading.Timer(float(Configuration.EXT_CYCLE_DURATION), cycleOFF)
    timer.start()
    logging.info("Extraction cycle started.")


def cycleOFF():
    global EXTRACTION_IN_CYCLE
    EXTRACTION_IN_CYCLE = False
    turnOFF()
    logging.info("Extraction cycle finished.")


def turnON():
    RCTransmitter.sendCommand(RCTransmitter.EXTRACTION_ON)
    logging.info("Extraction turned on.")


def turnOFF():
    RCTransmitter.sendCommand(RCTransmitter.EXTRACTION_OFF)
    logging.info("Extraction turned off.")


def autoAdjust():
    if Configuration.DAY:
        if Receiver.TEMP >= Configuration.MAX_DAY_TEMP or Receiver.HUM >= Configuration.MAX_DAY_HUM:
            turnON()
        else:
            if not EXTRACTION_IN_CYCLE:
                turnOFF()
    else:
        if Receiver.TEMP >= Configuration.MAX_NIGHT_TEMP or Receiver.HUM >= Configuration.MAX_NIGHT_HUM:
            turnON()
        else:
            if not EXTRACTION_IN_CYCLE:
                turnOFF()

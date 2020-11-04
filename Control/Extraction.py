import logging
import threading

import schedule

import Configuration
from Comm import RCTransmitter
from Sensors import Receiver

if Configuration.ELASTIC:
    from Comm import Elastic

EXTRACTION_ON = False
EXTRACTION_IN_CYCLE = False

AUTO_SCHEDULED = True


def scheduleAuto():
    schedule.every(Configuration.EXT_AUTO_FREQ).seconds.do(autoAdjust).tag('extraction-auto')
    scheduleCycle(Configuration.EXT_CYCLE_EVERY)
    logging.info("Auto Extraction scheduled every " + str(Configuration.EXT_AUTO_FREQ) + " seconds.")
    logging.info("Extraction cycles scheduled every " + str(Configuration.EXT_CYCLE_EVERY) + " seconds for " +
                 str(Configuration.EXT_CYCLE_DURATION) + " seconds.")


def reScheduleAuto():
    if not AUTO_SCHEDULED:
        schedule.every(Configuration.EXT_AUTO_FREQ).seconds.do(autoAdjust).tag('extraction-auto')


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
    global EXTRACTION_ON
    if not EXTRACTION_ON:
        RCTransmitter.sendCommand(RCTransmitter.EXTRACTION_ON)
        EXTRACTION_ON = True
        logging.info("Extraction turned on.")
        if Configuration.ELASTIC:
            Elastic.saveEvent("Extraction", "On", "Extraction turned off.")


def turnOFF():
    global EXTRACTION_ON
    if EXTRACTION_ON:
        RCTransmitter.sendCommand(RCTransmitter.EXTRACTION_OFF)
        EXTRACTION_ON = False
        logging.info("Extraction turned off.")
        if Configuration.ELASTIC:
            Elastic.saveEvent("Extraction", "Off", "Extraction turned off.")


def autoAdjust():
    if Configuration.DAY:
        if float(Receiver.TEMP) >= Configuration.MAX_DAY_TEMP or float(Receiver.HUM) >= Configuration.MAX_DAY_HUM:
            turnON()
        else:
            if not EXTRACTION_IN_CYCLE:
                turnOFF()
    else:
        if float(Receiver.TEMP) >= Configuration.MAX_NIGHT_TEMP or float(Receiver.HUM) >= Configuration.MAX_NIGHT_HUM:
            turnON()
        else:
            if not EXTRACTION_IN_CYCLE:
                turnOFF()

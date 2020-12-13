import logging
import threading

import schedule

import Configuration
from Comm import RCTransmitter
from Sensors import Receiver

if Configuration.ELASTIC:
    from Comm import Elastic

VENTILATION_ON = False
VENTILATION_IN_CYCLE = False

AUTO_SCHEDULED = True


def scheduleAuto():
    schedule.every(Configuration.VENT_AUTO_FREQ).seconds.do(autoAdjust).tag('ventilation-auto')
    scheduleCycle(Configuration.VENT_CYCLE_EVERY)
    logging.info("Auto Ventilation scheduled every " + str(Configuration.VENT_AUTO_FREQ) + " seconds.")
    logging.info("Ventilation cycles scheduled every " + str(Configuration.VENT_CYCLE_EVERY) + " seconds for " +
                 str(Configuration.VENT_CYCLE_DURATION) + " seconds.")


def reScheduleAuto():
    if not AUTO_SCHEDULED:
        schedule.every(Configuration.VENT_AUTO_FREQ).seconds.do(autoAdjust).tag('ventilation-auto')


def scheduleCycle(e):
    schedule.every(e).seconds.do(cycleON).tag('ventilation-cycle')


def cycleON():
    global VENTILATION_IN_CYCLE
    VENTILATION_IN_CYCLE = True
    turnON()
    timer = threading.Timer(float(Configuration.VENT_CYCLE_DURATION), cycleOFF)
    timer.start()
    logging.info("Ventilation cycle started.")


def cycleOFF():
    global VENTILATION_IN_CYCLE
    VENTILATION_IN_CYCLE = False
    turnOFF()
    logging.info("Ventilation cycle finished.")


def turnON():
    global VENTILATION_ON
    RCTransmitter.sendCommand(RCTransmitter.VENTILATION_ON)
    VENTILATION_ON = True
    logging.info("Ventilation turned on.")
    if Configuration.ELASTIC:
        Elastic.saveEvent("Ventilation", "On", "Ventilation turned on.")


def turnOFF():
    global VENTILATION_ON
    RCTransmitter.sendCommand(RCTransmitter.VENTILATION_OFF)
    VENTILATION_ON = False
    logging.info("Ventilation turned off.")
    if Configuration.ELASTIC:
        Elastic.saveEvent("Ventilation", "Off", "Ventilation turned off.")


def autoAdjust():
    if Configuration.DAY:
        if float(Receiver.TEMP) >= Configuration.MAX_DAY_TEMP or float(Receiver.HUM) >= Configuration.MAX_DAY_HUM:
            turnON()
        else:
            if not VENTILATION_IN_CYCLE:
                turnOFF()
    else:
        if float(Receiver.TEMP) >= Configuration.MAX_NIGHT_TEMP or float(Receiver.HUM) >= Configuration.MAX_NIGHT_HUM:
            turnON()
        else:
            if not VENTILATION_IN_CYCLE:
                turnOFF()

import logging
import subprocess

import schedule

import Configuration

FAN_ON = False


def scheduleAuto():
    schedule.every(30).seconds.do(autoControl)
    logging.info("System Cooling scheduled.")


def turnON():
    global FAN_ON
    FAN_ON = True
    logging.info("CPU Fan turned on.")


def turnOFF():
    global FAN_ON
    FAN_ON = False
    logging.info("CPU Fan turned off.")


def getCPUTemp():
    try:
        p = str(subprocess.check_output(['vcgencmd', 'measure_temp']))
        cpuTemp = p[p.index('=') + 1:p.rindex("'")]
    except Exception as e:
        cpuTemp = 0.0
        logging.error("Error obtaining CPU Temp. \n" + str(e))
    return float(cpuTemp)


def autoControl():
    cpuTemp = getCPUTemp()
    logging.debug("CPU Temp = " + str(cpuTemp) + " ºC")
    if cpuTemp >= Configuration.MAX_CPU_TEMP:
        turnON()
    else:
        turnOFF()

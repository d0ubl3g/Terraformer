import logging
import os
import subprocess
import threading

import Configuration

ILLUMINATION_ON = Configuration.ILLUMINATION_ON
ILLUMINATION_OFF = Configuration.ILLUMINATION_OFF
EXTRACTION_ON = Configuration.EXTRACTION_ON
EXTRACTION_OFF = Configuration.EXTRACTION_OFF
VENTILATION_ON = Configuration.VENTILATION_ON
VENTILATION_OFF = Configuration.VENTILATION_OFF
IRRIGATION_ON = Configuration.IRRIGATION_ON
IRRIGATION_OFF = Configuration.IRRIGATION_OFF

LOCK = threading.Lock()


def sendCommand(command):
    try:
        LOCK.acquire()
        dev_null = open(os.devnull, 'w')
        subprocess.run(
            ["rpi-rf_send", "-g", str(Configuration.GPIO_PIN), "-p", str(Configuration.PULSE_LENGTH), "-r", "50", "-t",
             "1", str(command)], stderr=dev_null, stdout=dev_null)
        logging.debug(str(command) + " transmitted vía RF.")
        LOCK.release()
    except Exception as e:
        logging.error(e)

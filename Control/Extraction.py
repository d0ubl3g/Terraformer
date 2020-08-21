import schedule
from colorama import Fore, Style

import Configuration
from Comm import RCTransmitter
from Sensors import Receiver

EXTRACTION_ON = False
EXTRACTION_IN_CYCLE = False


def scheduleAuto():
    schedule.every(10).seconds.do(autoAdjust)
    scheduleCycle(int(Configuration.EXT_CYCLE_EVERY), int(Configuration.EXT_CYCLE_DURATION))
    print(Fore.LIGHTGREEN_EX + "[*] Auto Extraction + Cycles scheduled.")


def scheduleCycle(e, d):
    schedule.every(e).minutes.do(cycleON)
    schedule.every(e+d).minutes.do(cycleOFF)


def autoAdjust():
    if Receiver.TEMP >= Configuration.ENV_MAX_TEMP or Receiver.HUM >= Configuration.ENV_MAX_HUM:
        turnON()
    else:
        if not EXTRACTION_IN_CYCLE:
            turnOFF()


def cycleON():
    global EXTRACTION_IN_CYCLE
    EXTRACTION_IN_CYCLE = True
    turnON()


def cycleOFF():
    global EXTRACTION_IN_CYCLE
    EXTRACTION_IN_CYCLE = False
    turnOFF()


def turnON():
    RCTransmitter.sendCommand(RCTransmitter.EXTRACTION_ON)
    print(Fore.GREEN + "[*] Extraction turned on." + Style.RESET_ALL)


def turnOFF():
    RCTransmitter.sendCommand(RCTransmitter.EXTRACTION_OFF)
    print(Fore.YELLOW + "[*] Extraction turned off." + Style.RESET_ALL)

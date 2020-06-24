import schedule
from colorama import Fore, Style

import Configuration
from Comm import RCTransmitter
from Sensors import Receiver

EXTRACTION_ON = False
EXTRACTION_IN_CYCLE = False


def scheduleAuto():
    schedule.every(10).seconds.do(autoAdjust)
    # CYCLE
    print(Fore.LIGHTGREEN_EX + "[*] Auto Extraction + Cycles scheduled.")


def autoAdjust():
    if Receiver.TEMP >= Configuration.ENV_MAX_TEMP or Receiver.HUM >= Configuration.ENV_MAX_HUM:
        if not EXTRACTION_ON:
            turnON()
    else:
        if EXTRACTION_ON and not EXTRACTION_IN_CYCLE:
            turnOFF()


def turnON():
    RCTransmitter.sendCommand(RCTransmitter.EXTRACTION_ON)
    print(Fore.GREEN + "[*] Extraction turned on." + Style.RESET_ALL)


def turnOFF():
    RCTransmitter.sendCommand(RCTransmitter.EXTRACTION_OFF)
    print(Fore.YELLOW + "[*] Extraction turned off." + Style.RESET_ALL)

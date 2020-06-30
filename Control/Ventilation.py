import schedule
from colorama import Fore, Style

import Configuration
from Comm import RCTransmitter
from Sensors import Receiver

VENTILATION_ON = False
VENTILATION_IN_CYCLE = False


def scheduleAuto():
    schedule.every(10).seconds.do(autoAdjust)
    # CYCLE
    print(Fore.LIGHTGREEN_EX + "[*] Auto Extraction + Cycles scheduled.")


def turnON():
    RCTransmitter.sendCommand(RCTransmitter.VENTILATION_ON)
    print(Fore.GREEN + "[*] Ventilation turned on." + Style.RESET_ALL)


def turnOFF():
    RCTransmitter.sendCommand(RCTransmitter.VENTILATION_OFF)
    print(Fore.YELLOW + "[*] Ventilation turned off." + Style.RESET_ALL)


def autoAdjust():
    if Receiver.TEMP >= Configuration.ENV_MAX_TEMP or Receiver.HUM >= Configuration.ENV_MAX_HUM:
        turnON()
    else:
        if not VENTILATION_IN_CYCLE:
            turnOFF()

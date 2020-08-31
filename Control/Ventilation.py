import schedule
from colorama import Fore, Style

import Configuration
from Comm import RCTransmitter
from Sensors import Receiver

VENTILATION_ON = False
VENTILATION_IN_CYCLE = False


def scheduleAuto():
    schedule.every(int(Configuration.VENT_AUTO_FREQ)).seconds.do(autoAdjust)
    scheduleCycle(int(Configuration.VENT_CYCLE_EVERY), int(Configuration.VENT_CYCLE_DURATION))
    print(Fore.LIGHTGREEN_EX + "[*] Auto Ventilation scheduled every " + Configuration.VENT_AUTO_FREQ + " seconds.")
    print(Fore.LIGHTGREEN_EX + "[*] Extraction cycles scheduled every " + Configuration.VENT_CYCLE_EVERY +
          " minutes for " + Configuration.VENT_CYCLE_DURATION + " minutes.")


def scheduleCycle(e, d):
    schedule.every(e).minutes.do(cycleON)
    schedule.every(e+d).minutes.do(cycleOFF)


def cycleON():
    global VENTILATION_IN_CYCLE
    VENTILATION_IN_CYCLE = True
    turnON()
    print(Fore.GREEN + "[*] Ventilation cycle started." + Style.RESET_ALL)


def cycleOFF():
    global VENTILATION_IN_CYCLE
    VENTILATION_IN_CYCLE = False
    turnOFF()
    print(Fore.YELLOW + "[*] Ventilation cycle finished." + Style.RESET_ALL)


def turnON():
    RCTransmitter.sendCommand(RCTransmitter.VENTILATION_ON)
    print(Fore.LIGHTGREEN_EX + "[*] Ventilation turned on." + Style.RESET_ALL)


def turnOFF():
    RCTransmitter.sendCommand(RCTransmitter.VENTILATION_OFF)
    print(Fore.YELLOW + "[*] Ventilation turned off." + Style.RESET_ALL)


def autoAdjust():
    if Receiver.TEMP >= Configuration.ENV_MAX_TEMP or Receiver.HUM >= Configuration.ENV_MAX_HUM:
        turnON()
    else:
        if not VENTILATION_IN_CYCLE:
            turnOFF()

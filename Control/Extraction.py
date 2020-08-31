import schedule
from colorama import Fore, Style

import Configuration
from Comm import RCTransmitter
from Sensors import Receiver

EXTRACTION_ON = False
EXTRACTION_IN_CYCLE = False


def scheduleAuto():
    schedule.every(int(Configuration.EXT_AUTO_FREQ)).seconds.do(autoAdjust)
    scheduleCycle(int(Configuration.EXT_CYCLE_EVERY), int(Configuration.EXT_CYCLE_DURATION))
    print(Fore.LIGHTGREEN_EX + "[*] Auto Extraction scheduled every " + Configuration.EXT_AUTO_FREQ + " seconds.")
    print(Fore.LIGHTGREEN_EX + "[*] Extraction cycles scheduled every " + Configuration.EXT_CYCLE_EVERY +
          " minutes for " + Configuration.EXT_CYCLE_DURATION + " minutes.")


def scheduleCycle(e, d):
    schedule.every(e).minutes.do(cycleON)
    schedule.every(e+d).minutes.do(cycleOFF)


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


def cycleON():
    global EXTRACTION_IN_CYCLE
    EXTRACTION_IN_CYCLE = True
    turnON()
    print(Fore.LIGHTGREEN_EX + "[*] Extraction cycle started." + Style.RESET_ALL)


def cycleOFF():
    global EXTRACTION_IN_CYCLE
    EXTRACTION_IN_CYCLE = False
    turnOFF()
    print(Fore.YELLOW + "[*] Extraction cycle finished." + Style.RESET_ALL)


def turnON():
    RCTransmitter.sendCommand(RCTransmitter.EXTRACTION_ON)
    print(Fore.LIGHTGREEN_EX + "[*] Extraction turned on." + Style.RESET_ALL)


def turnOFF():
    RCTransmitter.sendCommand(RCTransmitter.EXTRACTION_OFF)
    print(Fore.YELLOW + "[*] Extraction turned off." + Style.RESET_ALL)

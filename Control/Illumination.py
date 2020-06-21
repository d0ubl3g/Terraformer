import schedule
import Configuration
from colorama import Fore, Style
from Comm import RCTransmitter

ILLU_ON = False


def schedule():
    schedule.every().day.at(Configuration.ILLU_START_HOUR).do(turnON)
    schedule.every().day.at(Configuration.ILLU_STOP_HOUR).do(turnOFF)
    print(Fore.LIGHTGREEN_EX + "[*] Illumination scheduled.")


def turnON():
    RCTransmitter.sendCommand(RCTransmitter.ILLUMINATION_ON)
    print(Fore.GREEN + "[*] Illumination turned on." + Style.RESET_ALL)


def turnOFF():
    RCTransmitter.sendCommand(RCTransmitter.ILLUMINATION_OFF)
    print(Fore.YELLOW + "[*] Illumination turned off." + Style.RESET_ALL)

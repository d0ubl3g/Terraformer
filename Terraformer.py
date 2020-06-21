import time

import schedule
from colorama import init, Fore, Style

import Configuration
from Control import Illumination, Extraction
from System import Cooling
from ThermoHygro import Receiver

init()

print(Style.BRIGHT + Fore.BLUE + "Terraformer starting..." + Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + "[i] Loading configuration." + Style.RESET_ALL)
if Configuration.CONFIGURATION_SET:
    print(Fore.LIGHTGREEN_EX + "[*] Configuration found." + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "[ì] Initializing System Cooling..." + Style.RESET_ALL)
    Cooling.scheduleAuto()
    print(Fore.LIGHTBLUE_EX + "[i] Initializing ThermoHygrometer..." + Style.RESET_ALL)
    Receiver.scheduleAuto()
    print(Fore.LIGHTBLUE_EX + "[i] Initializing Illumination..." + Style.RESET_ALL)
    Illumination.schedule()
    print(Fore.LIGHTBLUE_EX + "[i] Initializing Extraction..." + Style.RESET_ALL)
    if Configuration.EXT_MODE == "auto":
        Extraction.scheduleAuto()
    else:
        print("Schedule")
    while True:
        schedule.run_pending()
        time.sleep(5)

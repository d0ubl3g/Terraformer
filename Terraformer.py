import time

import schedule
from colorama import init, Fore, Style

import Configuration
from Control import Illumination, Extraction, Ventilation
from Sensors import Receiver
from System import Cooling

init()

print(Style.BRIGHT + Fore.BLUE + "Terraformer starting..." + Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + "[i] Loading configuration." + Style.RESET_ALL)
Configuration.initializeDynamicConf()
if Configuration.CONFIGURATION_SET:
    print(Fore.LIGHTGREEN_EX + "[*] Configuration found." + Style.RESET_ALL)
    if Configuration.ENV_PHASE == "veg":
        print(Fore.LIGHTBLUE_EX + "[i] Vegetative phase configured.")
    elif Configuration.ENV_PHASE == "flow":
        print(Fore.LIGHTBLUE_EX + "[i] Flowering phase configured.")
    elif Configuration.ENV_PHASE == "dry":
        print(Fore.LIGHTBLUE_EX + "[i] Dry phase configured.")
    print(Fore.LIGHTBLUE_EX + "[ì] Initializing System Cooling..." + Style.RESET_ALL)
    Cooling.scheduleAuto()
    print(Fore.LIGHTBLUE_EX + "[i] Initializing Sensors..." + Style.RESET_ALL)
    Receiver.scheduleAuto()
    print(Fore.LIGHTBLUE_EX + "[i] Initializing Illumination..." + Style.RESET_ALL)
    Illumination.scheduleHours()
    print(Fore.LIGHTBLUE_EX + "[i] Initializing Extraction..." + Style.RESET_ALL)
    if Configuration.EXT_MODE == "auto":
        Extraction.scheduleAuto()
    else:
        print(Fore.RED + "[NOT IMPLEMENTED] Schedule Cycle" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "[i] Initializing Ventilation..." + Style.RESET_ALL)
    if Configuration.VENT_MODE == "auto":
        Ventilation.scheduleAuto()
    else:
        print(Fore.RED + "[NOT IMPLEMENTED] Schedule Cycle" + Style.RESET_ALL)
    while True:
        schedule.run_pending()
        time.sleep(5)
else:
    print(Fore.RED + "[!] Configuration is not set.")

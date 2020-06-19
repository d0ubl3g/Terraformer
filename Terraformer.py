import Configuration
from System import Cooling
import schedule
import time
from colorama import init, Fore, Style

init()

print(Style.BRIGHT + Fore.BLUE + "Terraformer starting..." + Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + "[i] Loading configuration." + Style.RESET_ALL)
if Configuration.CONFIGURATION_SET:
    print(Fore.LIGHTGREEN_EX + "[*] Configuration found." + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "[ì] Initializing System Cooling..." + Style.RESET_ALL)
    Cooling.scheduleAuto()
    while True:
        schedule.run_pending()
        time.sleep(5)

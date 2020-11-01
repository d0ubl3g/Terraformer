import argparse
import logging
import threading
import time

import schedule
from colorama import init, Fore, Style

import Configuration
from Control import Illumination, Extraction, Ventilation
from Modules import Banner, Interactive
from Sensors import Receiver
from System import Cooling

if Configuration.ELASTIC:
    from Comm import Elastic

init()
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='terraformer.log', level=logging.DEBUG, filemode='w')
logging.getLogger('schedule').setLevel(logging.WARNING)

parser = argparse.ArgumentParser()
parser.add_argument("-N", "--night", help="Start in Night mode", action="store_true")
parser.add_argument("-R", "--receiver", help="RF Code Receiver mode", action="store_true")
parser.add_argument("-D", "--daemon", help="Run in daemon mode. No Interactive console.", action="store_true")
args = parser.parse_args()

Banner.printBanner()
print(Style.BRIGHT + Fore.BLUE + "Terraformer starting..." + Style.RESET_ALL)
logging.info("Loading configuration...")
Configuration.initializeDynamicConf()
if args.night:
    Configuration.DAY = False
if Configuration.CONFIGURATION_SET:
    logging.info("Configuration loaded successfully.")
    if Configuration.ELASTIC:
        Elastic.initialize()
    if Configuration.ENV_PHASE == "veg":
        logging.info("Vegetative phase configured.")
    elif Configuration.ENV_PHASE == "flow":
        logging.info("Flowering phase configured.")
    elif Configuration.ENV_PHASE == "dry":
        logging.info("Dry phase configured.")
    logging.info("Initializing System Cooling...")
    Cooling.scheduleAuto()
    logging.info("Initializing Sensors...")
    Receiver.scheduleAuto()
    logging.info("Initializing Illumination...")
    Illumination.scheduleHours()
    logging.info("Initializing Extraction...")
    if Configuration.EXT_MODE == "auto":
        Extraction.scheduleAuto()
    else:
        logging.error("[NOT IMPLEMENTED] Ext Schedule Cycle")
    logging.info("Initializing Ventilation...")
    if Configuration.VENT_MODE == "auto":
        Ventilation.scheduleAuto()
    else:
        logging.error("[NOT IMPLEMENTED] Vent Schedule Cycle")
    if not args.daemon:
        threading.Thread(target=Interactive.start).start()
    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    logging.warning("Configuration not set.")

import subprocess

import schedule
from colorama import Fore, Style

from Control import Extraction, Illumination, Ventilation
from Sensors import Receiver


def printMenu():
    print(Style.BRIGHT)
    print(" _____________________________ TERRAFORMER CONTROL _____________________________")
    print("| help : Print this menu                                                        |")
    print("| status : Print environment status (Temp, Hum, etc.)                           |")
    print("| extraction : Print extraction system status.                                  |")
    print("|     ... start : Start extraction system.                                      |")
    print("|     ... stop  : Stop extraction system.                                       |")
    print("|     ... auto  : Print autonomous extraction status                            |")
    print("|         ... start : Start autonomous extraction system.                       |")
    print("|         ... stop  : Stop autonomous extraction                                |")
    print("| illumination : Print illumination system status.                              |")
    print("|     ... start : Turn on illumination.                                         |")
    print("|     ... stop  : Turn off illumination.                                        |")
    print("| ventilation : Print ventilation system status.                                |")
    print("|     ... start : Start ventilation system.                                     |")
    print("|     ... stop  : Stop ventilation system.                                      |")
    print("|     ... auto  : Print autonomous ventilation status                           |")
    print("|         ... start : Start autonomous ventilation system.                      |")
    print("|         ... stop  : Stop autonomous ventilation                               |")
    print("| log : Print real time logging                                                 |")
    print("| _____________________________________________________________________________ |")
    print(Style.RESET_ALL)


def printStatus():
    if Receiver.TEMP != "0.0" and Receiver.HUM != "0.0":
        print(Style.BRIGHT + Fore.LIGHTBLUE_EX)
        print("-------------- GROW ENVIRONMENT STATUS --------------")
        print("|       Temperature: " + Receiver.TEMP + "ºC     Humidity: " + Receiver.HUM + "%     |")
        print("-----------------------------------------------------")
        print(Style.RESET_ALL)
    else:
        print(Fore.MAGENTA + "\nSensors not initialized. Wait few seconds.\n" + Style.RESET_ALL)


def extractionStart():
    Extraction.turnON()
    print(Style.BRIGHT + Fore.GREEN + "\nExtraction system turned on.\n" + Style.RESET_ALL)


def extractionStop():
    Extraction.turnOFF()
    print(Style.BRIGHT + Fore.RED + "\nExtraction system turned off.\n" + Style.RESET_ALL)


def extractionAutoStart():
    Extraction.reScheduleAuto()
    print(Style.BRIGHT + Fore.GREEN + "\nExtraction autonomous system scheduled.\n" + Style.RESET_ALL)


def extractionAutoStop():
    schedule.clear('extraction-auto')
    Extraction.AUTO_SCHEDULED = False
    print(Style.BRIGHT + Fore.RED + "\nExtraction autonomous system unscheduled.\n" + Style.RESET_ALL)


def illuminationStart():
    Illumination.turnON()
    print(Style.BRIGHT + Fore.GREEN + "\nIllumination turned on.\n" + Style.RESET_ALL)


def illuminationStop():
    Illumination.turnOFF()
    print(Style.BRIGHT + Fore.RED + "\nIllumination turned off.\n" + Style.RESET_ALL)


def ventilationStart():
    Ventilation.turnON()
    print(Style.BRIGHT + Fore.GREEN + "\nVentilation system turned on.\n" + Style.RESET_ALL)


def ventilationStop():
    Ventilation.turnOFF()
    print(Style.BRIGHT + Fore.RED + "\nVentilation system turned on.\n" + Style.RESET_ALL)


def ventilationAutoStart():
    Ventilation.reScheduleAuto()
    print(Style.BRIGHT + Fore.GREEN + "\nVentilation autonomous system scheduled.\n" + Style.RESET_ALL)


def ventilationAutoStop():
    schedule.clear('ventilation-auto')
    Ventilation.AUTO_SCHEDULED = False
    print(Style.BRIGHT + Fore.RED + "\nVentilation autonomous system unscheduled.\n" + Style.RESET_ALL)


def printLog():
    subprocess.run(["tail", "-f", "/opt/Terraformer/terraformer.log"])


def execute(option):
    switcher = {
        "help": printMenu,
        "status": printStatus,
        "extraction start": extractionStart,
        "extraction stop": extractionStop,
        "extraction auto start": extractionAutoStart,
        "extraction auto stop": extractionAutoStop,
        "illumination start": illuminationStart,
        "illumination stop": illuminationStop,
        "ventilation start": ventilationStart,
        "ventilation stop": ventilationStop,
        "ventilation auto start": ventilationAutoStart,
        "ventilation auto stop": ventilationAutoStop,
        "log": printLog
    }
    func = switcher.get(option)
    func()


def start():
    printMenu()
    while True:
        try:
            option = input(Style.BRIGHT + "=> " + Style.RESET_ALL)
            execute(option)
        except Exception as e:
            print(Fore.RED + "\nInvalid option. Try with \"help\" \n" + Style.RESET_ALL)

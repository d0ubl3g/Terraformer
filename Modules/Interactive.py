import schedule
from colorama import Fore, Style

from Control import Extraction, Illumination, Ventilation


def printMenu():
    print("------------------------------ TERRAFORMER CONTROL ------------------------------")
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
    print("| ______________________________________________________________________________|")


def printStatus():
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX)
    print("-------------- GROW ENVIRONMENT STATUS --------------")
    print("|       Temperature %fºC    Humidity: %f%    |")
    print("|---------------------------------------------------|")


def extractionStart():
    Extraction.turnON()


def extractionStop():
    Extraction.turnOFF()


def extractionAutoStart():
    Extraction.reScheduleAuto()


def extractionAutoStop():
    schedule.clear('extraction-auto')
    Extraction.AUTO_SCHEDULED = False


def illuminationStart():
    Illumination.turnON()


def illuminationStop():
    Illumination.turnOFF()


def ventilationStart():
    Ventilation.turnON()


def ventilationStop():
    Ventilation.turnOFF()


def ventilationAutoStart():
    Ventilation.reScheduleAuto()


def ventilationAutoStop():
    schedule.clear('ventilation-auto')
    Ventilation.AUTO_SCHEDULED = False


def execute(option):
    switcher = {
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
        "ventilation auto stop": ventilationAutoStop
    }
    func = switcher.get(option, lambda: "Invalid option")
    func()


def start():
    while True:
        printMenu()
        option = input("")
        execute(option)

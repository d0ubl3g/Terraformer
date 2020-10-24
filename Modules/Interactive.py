import schedule
from colorama import Fore, Style

from Control import Extraction, Illumination, Ventilation
from Sensors import Receiver


def printMenu():
    print(Style.BRIGHT)
    print("------------------------------ TERRAFORMER CONTROL ------------------------------")
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
    print("| ______________________________________________________________________________|")


def printStatus():
    if Receiver.TEMP != 0.0 and Receiver.HUM != 0.0:
        print(Style.BRIGHT + Fore.LIGHTBLUE_EX)
        print("-------------- GROW ENVIRONMENT STATUS --------------")
        print("|       Temperature: " + str(Receiver.TEMP) + "     Humidity: " + str(Receiver.HUM + "%") + "    |")
        print("|---------------------------------------------------|")
        print(Style.RESET_ALL)
    else:
        print(Fore.MAGENTA + "Sensors not initialized. Wait few seconds.")


def extractionStart():
    Extraction.turnON()
    print(Style.BRIGHT + Fore.GREEN + "Extraction system turned on." + Style.RESET_ALL)


def extractionStop():
    Extraction.turnOFF()
    print(Style.BRIGHT + Fore.RED + "Extraction system turned off." + Style.RESET_ALL)


def extractionAutoStart():
    Extraction.reScheduleAuto()
    print(Style.BRIGHT + Fore.GREEN + "Extraction autonomous system scheduled." + Style.RESET_ALL)


def extractionAutoStop():
    schedule.clear('extraction-auto')
    Extraction.AUTO_SCHEDULED = False
    print(Style.BRIGHT + Fore.RED + "Extraction autonomous system unscheduled." + Style.RESET_ALL)


def illuminationStart():
    Illumination.turnON()
    print(Style.BRIGHT + Fore.GREEN + "Illumination turned on." + Style.RESET_ALL)


def illuminationStop():
    Illumination.turnOFF()
    print(Style.BRIGHT + Fore.RED + "Illumination turned off." + Style.RESET_ALL)


def ventilationStart():
    Ventilation.turnON()
    print(Style.BRIGHT + Fore.GREEN + "Ventilation system turned on." + Style.RESET_ALL)


def ventilationStop():
    Ventilation.turnOFF()
    print(Style.BRIGHT + Fore.RED + "Ventilation system turned on." + Style.RESET_ALL)


def ventilationAutoStart():
    Ventilation.reScheduleAuto()
    print(Style.BRIGHT + Fore.GREEN + "Ventilation autonomous system scheduled." + Style.RESET_ALL)


def ventilationAutoStop():
    schedule.clear('ventilation-auto')
    Ventilation.AUTO_SCHEDULED = False
    print(Style.BRIGHT + Fore.RED + "Ventilation autonomous system unscheduled." + Style.RESET_ALL)


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
        "ventilation auto stop": ventilationAutoStop
    }
    func = switcher.get(option)
    func()


def start():
    printMenu()
    while True:
        try:
            option = input("=> " + Style.RESET_ALL)
            execute(option)
        except Exception as e:
            print(Fore.RED + "\n Invalid option. Try with \"help\"" + Style.RESET_ALL)

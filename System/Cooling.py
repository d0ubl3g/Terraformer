import subprocess

import schedule
from colorama import Style, Fore

import Configuration

FAN_ON = False


def scheduleAuto():
    schedule.every(30).seconds.do(autoControl)
    print(Fore.LIGHTGREEN_EX + "[*] System Cooling scheduled." + Style.RESET_ALL)


def turnON():
    global FAN_ON
    FAN_ON = True
    print(Fore.LIGHTMAGENTA_EX + "[+] Turning on CPU Fan..." + Style.RESET_ALL)


def turnOFF():
    global FAN_ON
    FAN_ON = False
    print(Fore.MAGENTA + "[-] Turning off CPU Fan..." + Style.RESET_ALL)


def getCPUTemp():
    try:
        p = subprocess.check_output(['vcgencmd', 'measure_temp'])
        cpuTemp = float(subprocess.check_output(['egrep', '-o', '[0-9]*\\.[0-9]*'], stdin=p))
    except Exception as e:
        cpuTemp = 0.0
        print(Fore.RED + "[!] Error obtaining CPU Temp.")
        print(str(e) + Style.RESET_ALL)
    return cpuTemp


def autoControl():
    cpuTemp = getCPUTemp()
    print(Fore.LIGHTBLUE_EX + "[i] CPU Temp = " + str(cpuTemp) + " ºC")
    if cpuTemp >= Configuration.MAX_CPU_TEMP:
        if not FAN_ON:
            turnON()
    else:
        if FAN_ON:
            turnOFF()

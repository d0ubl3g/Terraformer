import subprocess

import schedule

import Configuration


def scheduleAuto():
    schedule.every(30).seconds.do(autoControl())


def turnON():
    print("Turning on CPU Fan...")


def turnOFF():
    print("Turning off CPU Fan...")


def getCPUTemp():
    cpuTemp = 0.0
    try:
        p = subprocess.check_output(['vcgencmd', 'measure_temp'])
        cpuTemp = float(subprocess.check_output(['egrep', '-o', '[0-9]*\\.[0-9]*'], stdin=p))
    except Exception as e:
        print(e)
    return cpuTemp


def autoControl():
    if getCPUTemp() >= Configuration.MAX_CPU_TEMP:
        turnON()
    else:
        turnOFF()

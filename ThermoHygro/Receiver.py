import sys
import Adafruit_DHT
import schedule
import Configuration
from colorama import Fore, Style

TEMP = "0.0"
HUM = "0.0"


def scheduleAuto():
    schedule.every(20).seconds.do(getTempHum)


def getTempHum():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 15) #SENSOR , GPIOPIN
    global TEMP
    global HUM
    if humidity is not None and temperature is not None:
        value = "{0:0.1f},{1:0.1f}".format(temperature, humidity)
        TEMP = "{0:0.1f}".format(temperature)
        HUM = "{0:0.1f}".format(humidity)
        print(Fore.LIGHTGREEN_EX + "[i] Temperature: " + TEMP + "ºC " + "Humidity: " + HUM + "%" + Style.RESET_ALL)
        return value
    else:
        print(Fore.RED + "Error receiving data." + Style.RESET_ALL)
        return None

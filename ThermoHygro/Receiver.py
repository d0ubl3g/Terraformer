import sys
import Adafruit_DHT
import schedule
from colorama import Fore, Style

TEMP = "0.0"
HUM = "0.0"

def schedule():
    schedule.every(20).seconds.do(getTempHum())

def getTempHum():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 15) #SENSOR , GPIOPIN
    if humidity is not None and temperature is not None:
        value = "{0:0.1f},{1:0.1f}".format(temperature, humidity)
        temp = "{0:0.1f}".format(temperature)
        hum = "{0:0.1f}".format(humidity)
        print(Fore.LIGHTGREEN_EX + "[i] Temperature: " + temp + "ºC " + "Humidity: " + hum + "%" + Style.RESET_ALL)
        return value
    else:
        print(Fore.RED + "Error receiving data." + Style.RESET_ALL)
        return None

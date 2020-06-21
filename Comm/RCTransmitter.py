import subprocess

GPIO_PIN = 17
PULSE_LENGTH = 176
ILLUMINATION_ON = "5264691"
ILLUMINATION_OFF = "5264700"
EXTRACTION_ON = "5264835"
EXTRACTION_OFF = "5264844"
VENTILATION_ON = "5265155"
VENTILATION_OFF = "5265164"
CO2_ON = "co2_on"
CO2_OFF = "co2_off"
ALL_ON = "5272835"
ALL_OFF = "5272844"


def sendCommand(command):
    p = subprocess.run(["rpi-rf_send", "-g", GPIO_PIN, "-p", PULSE_LENGTH, "-t", "1", command])

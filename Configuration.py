import configparser
import os

working_directory = os.path.dirname(os.path.abspath(__file__))

config = configparser.ConfigParser()
config.read(working_directory + '/Terraformer.conf')

# DEFAULT #
default = config['DEFAULT']
CONFIGURATION_SET = bool(default['Configured'])
PASSWORD = default['Password']
MAX_CPU_TEMP = default['MaxCPUTemp']

# ENVIRONMENT #
environment = config['ENVIRONMENT']
ENV_MAX_TEMP = environment['MaxTemp']
ENV_MIN_TEMP = environment['MinTemp']
ENV_MAX_HUM = environment['MaxHum']
ENV_MIN_HUM = environment['MinHum']

# ILLUMINATION #
illumination = config['ILLUMINATION']
ILLU_START_HOUR = illumination['StartHour']
ILLU_STOP_HOUR = illumination['StopHour']

# EXTRACTION #
extraction = config['EXTRACTION']
EXT_MODE = extraction['Mode']

# VENTILATION #
ventilation = config['VENTILATION']
VENT_MODE = ventilation['Mode']

# CO2 #
co2 = config['CO2']
CO2_MODE = co2['Mode']

import configparser
import os

working_directory = os.path.dirname(os.path.abspath(__file__))

config = configparser.ConfigParser()
config.read(working_directory + '/Terraformer.conf')

# DEFAULT #
default = config['DEFAULT']
CONFIGURATION_SET = bool(default['Configured'])
PASSWORD = default['Password']
MAX_CPU_TEMP = float(default['MaxCPUTemp'])

# ENVIRONMENT #
environment = config['ENVIRONMENT']
ENV_DATA_FREQ = environment['DataFreq']
ENV_MAX_TEMP = environment['MaxTemp']
ENV_MIN_TEMP = environment['MinTemp']
ENV_MAX_HUM = environment['MaxHum']
ENV_MIN_HUM = environment['MinHum']

# ILLUMINATION #
illumination = config['ILLUMINATION']
ILLU_START_HOUR = illumination['StartHour']
ILLU_STOP_HOUR = illumination['EndHour']

# EXTRACTION #
extraction = config['EXTRACTION']
EXT_MODE = extraction['Mode']
EXT_AUTO_FREQ = extraction['AutoFreq']
EXT_CYCLE_EVERY = extraction['CycleEvery']
EXT_CYCLE_DURATION = extraction['CycleDuration']

# VENTILATION #
ventilation = config['VENTILATION']
VENT_MODE = ventilation['Mode']
VENT_AUTO_FREQ = ventilation['AutoFreq']
VENT_CYCLE_EVERY = ventilation['CycleEvery']
VENT_CYCLE_DURATION = ventilation['CycleDuration']


# CO2 #
co2 = config['CO2']
CO2_MODE = co2['Mode']

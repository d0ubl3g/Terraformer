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
ENV_PHASE = environment['Phase']
ENV_DATA_FREQ = environment['DataFreq']
ENV_VEG_DAY_MAX_TEMP = environment['VegDayMaxTemp']
ENV_VEG_DAY_MIN_TEMP = environment['VegDayMinTemp']
ENV_VEG_DAY_MAX_HUM = environment['VegDayMaxHum']
ENV_VEG_DAY_MIN_HUM = environment['VegDayMinHum']
ENV_VEG_NIGHT_MAX_TEMP = environment['VegNightMaxTemp']
ENV_VEG_NIGHT_MIN_TEMP = environment['VegNightMinTemp']
ENV_VEG_NIGHT_MAX_HUM = environment['VegNightMaxHum']
ENV_VEG_NIGHT_MIN_HUM = environment['VegNightMinHum']
ENV_FLOW_DAY_MAX_TEMP = environment['FlowDayMaxTemp']
ENV_FLOW_DAY_MIN_TEMP = environment['FlowDayMinTemp']
ENV_FLOW_DAY_MAX_HUM = environment['FlowDayMaxHum']
ENV_FLOW_DAY_MIN_HUM = environment['FlowDayMinHum']
ENV_FLOW_NIGHT_MAX_TEMP = environment['FlowNightMaxTemp']
ENV_FLOW_NIGHT_MIN_TEMP = environment['FlowNightMinTemp']
ENV_FLOW_NIGHT_MAX_HUM = environment['FlowNightMaxHum']
ENV_FLOW_NIGHT_MIN_HUM = environment['FlowNightMinHum']

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

# DYNAMIC CONF #
DAY = True
MAX_DAY_TEMP = 0.0
MIN_DAY_TEMP = 0.0
MAX_NIGHT_TEMP = 0.0
MIN_NIGHT_TEMP = 0.0
MAX_DAY_HUM = 0.0
MIN_DAY_HUM = 0.0
MAX_NIGHT_HUM = 0.0
MIN_NIGHT_HUM = 0.0


def initializeDynamicConf():
    global MAX_DAY_TEMP
    global MIN_DAY_TEMP
    global MAX_NIGHT_TEMP
    global MIN_NIGHT_TEMP
    global MAX_DAY_HUM
    global MIN_DAY_HUM
    global MAX_NIGHT_HUM
    global MIN_NIGHT_HUM
    if ENV_PHASE == "veg":
        MAX_DAY_TEMP = ENV_VEG_DAY_MAX_TEMP
        MIN_DAY_TEMP = ENV_VEG_DAY_MIN_TEMP
        MAX_NIGHT_TEMP = ENV_VEG_NIGHT_MAX_TEMP
        MIN_NIGHT_TEMP = ENV_VEG_NIGHT_MIN_TEMP
        MAX_DAY_HUM = ENV_VEG_DAY_MAX_HUM
        MIN_DAY_HUM = ENV_VEG_DAY_MIN_HUM
        MAX_NIGHT_HUM = ENV_VEG_NIGHT_MAX_HUM
        MIN_NIGHT_HUM = ENV_VEG_NIGHT_MIN_HUM
    elif ENV_PHASE == "flow":
        MAX_DAY_TEMP = ENV_FLOW_DAY_MAX_TEMP
        MIN_DAY_TEMP = ENV_FLOW_DAY_MIN_TEMP
        MAX_NIGHT_TEMP = ENV_FLOW_NIGHT_MAX_TEMP
        MIN_NIGHT_TEMP = ENV_FLOW_NIGHT_MIN_TEMP
        MAX_DAY_HUM = ENV_FLOW_DAY_MAX_HUM
        MIN_DAY_HUM = ENV_FLOW_DAY_MIN_HUM
        MAX_NIGHT_HUM = ENV_FLOW_NIGHT_MAX_HUM
        MIN_NIGHT_HUM = ENV_FLOW_NIGHT_MIN_HUM

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
ELASTIC = bool(default['Elastic'])

# ENVIRONMENT #
environment = config['ENVIRONMENT']
ENV_PHASE = environment['Phase']
ENV_DATA_FREQ = int(environment['DataFreq'])
ENV_VEG_DAY_MAX_TEMP = float(environment['VegDayMaxTemp'])
ENV_VEG_DAY_MIN_TEMP = float(environment['VegDayMinTemp'])
ENV_VEG_DAY_MAX_HUM = float(environment['VegDayMaxHum'])
ENV_VEG_DAY_MIN_HUM = float(environment['VegDayMinHum'])
ENV_VEG_NIGHT_MAX_TEMP = float(environment['VegNightMaxTemp'])
ENV_VEG_NIGHT_MIN_TEMP = float(environment['VegNightMinTemp'])
ENV_VEG_NIGHT_MAX_HUM = float(environment['VegNightMaxHum'])
ENV_VEG_NIGHT_MIN_HUM = float(environment['VegNightMinHum'])
ENV_FLOW_DAY_MAX_TEMP = float(environment['FlowDayMaxTemp'])
ENV_FLOW_DAY_MIN_TEMP = float(environment['FlowDayMinTemp'])
ENV_FLOW_DAY_MAX_HUM = float(environment['FlowDayMaxHum'])
ENV_FLOW_DAY_MIN_HUM = float(environment['FlowDayMinHum'])
ENV_FLOW_NIGHT_MAX_TEMP = float(environment['FlowNightMaxTemp'])
ENV_FLOW_NIGHT_MIN_TEMP = float(environment['FlowNightMinTemp'])
ENV_FLOW_NIGHT_MAX_HUM = float(environment['FlowNightMaxHum'])
ENV_FLOW_NIGHT_MIN_HUM = float(environment['FlowNightMinHum'])

# ILLUMINATION #
ILLU_START_HOUR = ""
ILLU_STOP_HOUR = ""
illumination = config['ILLUMINATION']
ILLU_VEG_START_HOUR = illumination['VegStartHour']
ILLU_VEG_STOP_HOUR = illumination['VegEndHour']
ILLU_FLOW_START_HOUR = illumination['FlowStartHour']
ILLU_FLOW_STOP_HOUR = illumination['FlowEndHour']

# EXTRACTION #
extraction = config['EXTRACTION']
EXT_MODE = extraction['Mode']
EXT_AUTO_FREQ = int(extraction['AutoFreq'])
EXT_CYCLE_EVERY = int(extraction['CycleEvery'])
EXT_CYCLE_DURATION = int(extraction['CycleDuration'])

# VENTILATION #
ventilation = config['VENTILATION']
VENT_MODE = ventilation['Mode']
VENT_AUTO_FREQ = int(ventilation['AutoFreq'])
VENT_CYCLE_EVERY = int(ventilation['CycleEvery'])
VENT_CYCLE_DURATION = int(ventilation['CycleDuration'])

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
    global ILLU_START_HOUR
    global ILLU_STOP_HOUR
    global MAX_DAY_TEMP
    global MIN_DAY_TEMP
    global MAX_NIGHT_TEMP
    global MIN_NIGHT_TEMP
    global MAX_DAY_HUM
    global MIN_DAY_HUM
    global MAX_NIGHT_HUM
    global MIN_NIGHT_HUM
    if ENV_PHASE == "veg":
        ILLU_START_HOUR = ILLU_VEG_START_HOUR
        ILLU_STOP_HOUR = ILLU_VEG_STOP_HOUR
        MAX_DAY_TEMP = ENV_VEG_DAY_MAX_TEMP
        MIN_DAY_TEMP = ENV_VEG_DAY_MIN_TEMP
        MAX_NIGHT_TEMP = ENV_VEG_NIGHT_MAX_TEMP
        MIN_NIGHT_TEMP = ENV_VEG_NIGHT_MIN_TEMP
        MAX_DAY_HUM = ENV_VEG_DAY_MAX_HUM
        MIN_DAY_HUM = ENV_VEG_DAY_MIN_HUM
        MAX_NIGHT_HUM = ENV_VEG_NIGHT_MAX_HUM
        MIN_NIGHT_HUM = ENV_VEG_NIGHT_MIN_HUM
    elif ENV_PHASE == "flow":
        ILLU_START_HOUR = ILLU_FLOW_START_HOUR
        ILLU_STOP_HOUR = ILLU_FLOW_STOP_HOUR
        MAX_DAY_TEMP = ENV_FLOW_DAY_MAX_TEMP
        MIN_DAY_TEMP = ENV_FLOW_DAY_MIN_TEMP
        MAX_NIGHT_TEMP = ENV_FLOW_NIGHT_MAX_TEMP
        MIN_NIGHT_TEMP = ENV_FLOW_NIGHT_MIN_TEMP
        MAX_DAY_HUM = ENV_FLOW_DAY_MAX_HUM
        MIN_DAY_HUM = ENV_FLOW_DAY_MIN_HUM
        MAX_NIGHT_HUM = ENV_FLOW_NIGHT_MAX_HUM
        MIN_NIGHT_HUM = ENV_FLOW_NIGHT_MIN_HUM

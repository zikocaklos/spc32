import tsl2561

def read_light():
    sensor = tsl2561.TSL2561()
    return sensor.read()

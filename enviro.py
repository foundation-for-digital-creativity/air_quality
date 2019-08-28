import triot

from inventthings.simple_sensor import register_sensor

from inventthings.sensors import BME280, VEML6075, APDS9960 # HDC1080, BMP280

expansion_i2c = triot.expansion_i2c

#print("init envirosensors")

try:
    weather_sensor = BME280(expansion_i2c)
    uv_sensor = VEML6075(expansion_i2c)
    light_sensor = APDS9960(expansion_i2c)

    register_sensor(weather_sensor)
except OSError:
    print('Failed to detect Sense Expansion')
    weather_sensor = None
    uv_sensor = None
    light_sensor = None

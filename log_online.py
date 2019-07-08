import triot
from inventthings.particulates import particulate_sensor as pm
import inventthings.iot

#start by turning light on as yellow so we know it's on!
triot.leds[0] = Colour('yellow')

# start the FAN please (on the so the air quality starts sucking air in)
pm.enable_sensor=True
pm.enable_power=True

inventthings.iot.wlan_connect(ssid='THE_SSID', password='THE_PASSWORD')
nm = inventthings.iot.NetworkManager()

def on_connected():
    conn = inventthings.iot.InventThingsConnection(key="YOUR_THING_KEY")
    particulates = inventthings.iot.Endpoint("pm2.5",inventthings.iot.PARTICULATES)
    sensors = inventthings.iot.EndpointSet([particulates])
    conn.register_sensor_set(sensors.ep_descriptions())
    while True:
        triot.leds[0] = Colour('green')
        conn.record_data(sensors.record_readings([pm.pm_25]))
        time.sleep(1)
        triot.leds.clear()
        time.sleep(10)

nm.onConnect = on_connected
nm.start_loop()

import inventthings.iot
import inventthings.webserver

# connect to WiFi
wlan = inventthings.iot.wlan_connect()
# start webserver on triot
inventthings.webserver.run_server(wlan)

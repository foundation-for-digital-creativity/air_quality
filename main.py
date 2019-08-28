import triot
#start by turning light on as yellow so we know it's on!
triot.leds[0] = Colour('yellow')

#setup the expansion port
import inventthings
inventthings.expansion_i2c = triot.expansion_i2c

#import the sensors
from inventthings.particulates import particulate_sensor as pm
from inventthings.gps import gps_sensor as gps

# it's easier to use ddd.ddddddd than ddd,mm.mmmmmms so import a convertor
from inventthings.gps import deg_decmin_to_dec_deg
import utime as time

 
# open a file that we'll save the data into
filename = "filename.csv"
csv_file = open(filename,"a+")
 
# start the FAN please (on the so the air quality starts sucking air in)
pm.enable_sensor=True
pm.enable_power=True
 

row_count = 0

# run for ever, (or until we disconnect the power or press control-c!
while True:
    # increment the row counter
    row_count = row_count +1

    # change the light to green show we're reading data
    triot.leds[0] = Colour('green')

    # add a row of data to the file. the {} will be replaced by the values in 
    print("{},{},{},{},{}".format(row_count,
                               deg_decmin_to_dec_deg(gps.lat),
                               deg_decmin_to_dec_deg(gps.lon),
                               pm.pm_10,
                               pm.pm_25), file=csv_file)
    # flush makes the data go to the file immediately, rather than buffered in memory (which might mean it gets lost if the power is pulled suddenly)
    csv_file.flush()
    # pause for a second
    time.sleep(1)
    # turn off the light to show we've finished the read
    triot.leds.clear()
    # pause for a bit before going round the loop again
    time.sleep(10)

 
# just in case we leave the loop, display a red light
triot.leds[1] = Colour('red')
# close the file as we're done with it
csv_file.close()

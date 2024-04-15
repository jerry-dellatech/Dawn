import sys
import pins
from valve import Valve
from pump import VacuumPump
from time import sleep

"""Main file. Handles physical pin inputs; toggles valves & vacuum pump"""

#This is a ton of boilerplate code to handle valve control
#I built this on a "functional programming paradigm" instead of OOP as I am used to C. Infact, most of this code was converted from C

#A lot of this boilerplate is super excessive but I thought I would include it to simplify the valves for non coders who have to look at this
#If you really want, this whole thing could be 10 lines


def main():
    # main loop
    while True:
        if pins.START.pullup_value() and pins.STOP.pullup_value(): 
            continue # IO conflict, ignore it
        
        if pins.START.pullup_value():
            pump.set_pump(VacuumPump.ON)
            sleep(0.1)
            valve.set_valve(Valve.OPEN)
        elif pins.STOP.pullup_value():
            valve.set_valve(Valve.CLOSED)
            sleep(0.1)
            pump.set_pump(VacuumPump.OFF)
            


# Call the main function
if __name__ == "__main__":

    # initialize relay and valve
    relays = pins.RELAY_CONTROLLER # get relay controller from pins.py

    pump = VacuumPump(pins.PUMP_RELAY, VacuumPump.OFF)
    valve = Valve(Valve.NORMAL_CLOSED, pins.VALVE_RELAY, Valve.CLOSED)

    # check relay connection
    if relays.begin() == False:
        print("The Qwiic Relay isn't connected to the system. Please check your connection")
        sys.exit()

    try:
        # run main loop
        main()
    finally:
        # turn off relays on exit
        relays.set_all_relays_off()

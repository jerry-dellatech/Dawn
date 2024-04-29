import sys
import pins
from valve import Valve
from pump import VacuumPump
from time import sleep

"""Main file. Handles physical pin inputs; toggles valves & vacuum pump"""

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

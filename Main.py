import qwiic_relay
from machine import Pin, I2C, RTC
from time import sleep
import sys

#This is a ton of boilerplate code to handle valve control
#I built this on a "functional programming paradigm" instead of OOP as I am used to C. Infact, most of this code was converted from C

#A lot of this boilerplate is super excessive but I thought I would include it to simplify the valves for non coders who have to look at this
#If you really want, this whole thing could be 10 lines




def main():
    # Initialize everything

    #insure to define initial state that makes sense
    solenoidname = Valve(ALWAYS_OPEN, 1, True)
    
    set_valve(solenoidname, OPEN)
    
    # Python init relay
    while True:
        if GPIO.input(1) and not GPIO.input(2):
            set_valve(solenoidname, CLOSED) #or something like that
        elif GPIO.input(2) and not GPIO.input(1):
            set_valve(solenoidname, OPEN) #or something like that
        else:
            sys.exit("IO Conflict")

            





# Define constants(carry over from C macros)
ALWAYS_OPEN = True
ALWAYS_CLOSED = False
OPEN = True
CLOSED = False
# Define valve
class Valve:
    def __init__(self, valve_type, connected_relay, state):
        self.valve_type = valve_type
        self.state = state

# Define function to set valve state
def set_valve(valve, open):
    if open:
        if valve.valve_type == ALWAYS_OPEN:
            relays.set_relay_off(valve.connected_relay)
            valve.state = True
        if valve.valve_type == ALWAYS_CLOSED:
            relays.set_relay_on(valve.connected_relay)
            valve.state = True
    else:
        if valve.valve_type == ALWAYS_OPEN:
            relays.set_relay_on(valve.connected_relay)
            valve.state = False
        if valve.valve_type == ALWAYS_CLOSED:
            relays.set_relay_off(valve.connected_relay)
            valve.state = False

relays = qwiic_relay.QwiicRelay(qwiic_relay.QUAD_RELAY_DEFUALT_ADDR)

if relays.begin() == False:
    print("The Qwiic Relay isn't connected to the system. Please check your connection")
    sys.exit()

# Call the main function
if __name__ == "__main__":
    main()


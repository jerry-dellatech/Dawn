import qwiic_relay
from machine import Pin, I2C, RTC
from time import sleep
import sys
import pins

#This is a ton of boilerplate code to handle valve control
#I built this on a "functional programming paradigm" instead of OOP as I am used to C. Infact, most of this code was converted from C

#A lot of this boilerplate is super excessive but I thought I would include it to simplify the valves for non coders who have to look at this
#If you really want, this whole thing could be 10 lines




def main():
    # Initialize everything

    # insure to define initial state that makes sense
    solenoidname = Valve(ALWAYS_OPEN, 1, True)
    
    solenoidname.set_valve(OPEN)
    
    # Python init relay
    while True:
        if pins.START.value() and not pins.STOP.value():
            solenoidname.set_valve(CLOSED) # or something like that
        elif pins.STOP.value() and not pins.START.value():
            solenoidname.set_valve(OPEN) # or something like that
        else:
            # sys.exit("IO Conflict")
            pass

            





# Define constants(carry over from C macros)
ALWAYS_OPEN = True
ALWAYS_CLOSED = False
OPEN = True
CLOSED = False
# Define valve
class Valve:
    def __init__(self, valve_type=ALWAYS_OPEN, connected_relay=1, state=True):
        self.valve_type = valve_type
        self.state = state
        self.connected_relay = connected_relay

    # Define function to set valve state
    def set_valve(self, open: bool):
        if open:
            if self.valve_type == ALWAYS_OPEN:
                relays.set_relay_off(self.connected_relay)
                self.state = True
            if self.valve_type == ALWAYS_CLOSED:
                relays.set_relay_on(self.connected_relay)
                self.state = True
        else:
            if self.valve_type == ALWAYS_OPEN:
                relays.set_relay_on(self.connected_relay)
                self.state = False
            if self.valve_type == ALWAYS_CLOSED:
                relays.set_relay_off(self.connected_relay)
                self.state = False

relays = qwiic_relay.QwiicRelay(qwiic_relay.QUAD_RELAY_DEFUALT_ADDR)

if relays.begin() == False:
    print("The Qwiic Relay isn't connected to the system. Please check your connection")
    sys.exit()

# Call the main function
if __name__ == "__main__":
    main()


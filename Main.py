import qwiic_relay
import sys
import pins
import relay

#This is a ton of boilerplate code to handle valve control
#I built this on a "functional programming paradigm" instead of OOP as I am used to C. Infact, most of this code was converted from C

#A lot of this boilerplate is super excessive but I thought I would include it to simplify the valves for non coders who have to look at this
#If you really want, this whole thing could be 10 lines

# Define constants(carry over from C macros)
ALWAYS_OPEN = True
ALWAYS_CLOSED = False
OPEN = True
CLOSED = False

# Define valve
class Valve:
    def __init__(self, valve_type, relay_controller, connected_relay, state=OPEN):
        self.valve_type = valve_type
        self.state = state
        self.relay_controller: relay.Relay = relay_controller
        self.connected_relay = connected_relay
        self.set_valve(state)

    # Define function to set valve state
    def set_valve(self, open: bool):
        # set relay state correctly for valve type
        valve_state = open if self.valve_type == ALWAYS_CLOSED else not open

        self.relay_controller.set_relay_state(self.connected_relay, valve_state)
        self.state = open


def main():
    # main loop
    while True:
        if pins.START.value() and pins.STOP.value(): 
            continue # IO conflict, ignore it

        if solenoidname.state == OPEN and pins.START.value():
            solenoidname.set_valve(CLOSED)
        elif solenoidname.state == CLOSED and pins.STOP.value():
            solenoidname.set_valve(OPEN)


# Call the main function
if __name__ == "__main__":

    # initialize relay and valve
    relays = relay.Relay(qwiic_relay.QUAD_RELAY_DEFUALT_ADDR, pins.I2C_DRIVER)
    solenoidname = Valve(ALWAYS_CLOSED, relays, 1, OPEN)

    # check relay connection
    if relays.begin() == False:
        print("The Qwiic Relay isn't connected to the system. Please check your connection")
        sys.exit()

    try:
        # run main loop
        main()
    except (KeyboardInterrupt, SystemExit):
        # turn off relays on exit
        relays.set_all_relays_off()

import sys
import pins
from valve import Valve

#This is a ton of boilerplate code to handle valve control
#I built this on a "functional programming paradigm" instead of OOP as I am used to C. Infact, most of this code was converted from C

#A lot of this boilerplate is super excessive but I thought I would include it to simplify the valves for non coders who have to look at this
#If you really want, this whole thing could be 10 lines


def main():
    # main loop
    while True:
        if pins.START.value() and pins.STOP.value(): 
            continue # IO conflict, ignore it

        if solenoidname.state == Valve.OPEN and pins.START.value():
            solenoidname.set_valve(Valve.CLOSED)
        elif solenoidname.state == Valve.CLOSED and pins.STOP.value():
            solenoidname.set_valve(Valve.OPEN)


# Call the main function
if __name__ == "__main__":

    # initialize relay and valve
    relays = pins.RELAY_CONTROLLER # get relay controller from pins.py
    solenoidname = Valve(Valve.NORMAL_CLOSED, relays, 1, Valve.CLOSED)

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

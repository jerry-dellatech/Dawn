import pins

"""Toggles all relays on board based on pin input"""

relay = pins.RELAY_CONTROLLER

def main_loop():
    if not relay.begin():
        print("Relay not connected!")
        return
    
    relay.set_all_relays_off()
    relay_on = False

    while True:
        if pins.START.value() and pins.STOP.value(): continue

        if not relay_on and pins.START.value():
            relay_on = True
            relay.set_all_relays_on()
        if relay_on and pins.STOP.value():
            relay.set_all_relays_off()
            relay_on = False

if __name__ == "__main__":
    try:
        main_loop()
    except (KeyboardInterrupt, SystemExit):
        # turns off relays if stop button is pressed
        relay.set_all_relays_off()
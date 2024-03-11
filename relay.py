import qwiic_relay

"""More QwiicRelay functions for convenience"""

class Relay(qwiic_relay.QwiicRelay):
    # easier use of variables to set relay state
    def set_relay_state(self, relay_num:int, state:bool): 
        self.set_relay_off(relay_num) if state else self.set_relay_on(relay_num)

    def __str__(self) -> str: # easy printing
        return f"""Relay 1 state: {self.get_relay_state(1)}
Relay 2 state: {self.get_relay_state(2)}
Relay 3 state: {self.get_relay_state(3)}
Relay 4 state: {self.get_relay_state(4)}
"""
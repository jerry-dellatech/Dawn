import qwiic_relay

"""Here in case modifications to QwiicRelay base class are needed"""

class Relay(qwiic_relay.QwiicRelay):
    def __str__(self) -> str: # easy printing
        return f"""Relay 1 state: {self.get_relay_state(1)}
Relay 2 state: {self.get_relay_state(2)}
Relay 3 state: {self.get_relay_state(3)}
Relay 4 state: {self.get_relay_state(4)}
"""
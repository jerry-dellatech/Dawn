from relay import Relay

"""Solenoid valve controller"""

class Valve:
    NORMAL_OPEN = True
    NORMAL_CLOSED = False
    OPEN = True
    CLOSED = False

    def __init__(self, valve_type, relay_controller, connected_relay, state=CLOSED):
        self.valve_type: bool = valve_type
        self.state = state
        self.relay_controller: Relay = relay_controller
        self.connected_relay: int = connected_relay
        self.set_valve(state)

    # Define function to set valve state
    def set_valve(self, open: bool) -> None:
        # set relay state correctly for valve type
        valve_state = open if self.valve_type == Valve.NORMAL_CLOSED else not open

        self.relay_controller.set_relay_state(self.connected_relay, valve_state)
        self.state = open
from single_relay import SingleRelay

"""Solenoid valve controller"""

class Valve:
    NORMAL_OPEN = True
    NORMAL_CLOSED = False
    OPEN = True
    CLOSED = False

    def __init__(self, valve_type:bool, relay:SingleRelay, state=CLOSED):
        self.valve_type = valve_type
        self.relay = relay
        self.set_valve(state)

    @property
    def state(self) -> bool:
        if self.valve_type == Valve.NORMAL_CLOSED:
            return self.relay.get_relay_state()
        return not self.relay.get_relay_state()

    # Define function to set valve state
    def set_valve(self, open: bool) -> None:
        # set relay state correctly for valve type
        valve_state = open if self.valve_type == Valve.NORMAL_CLOSED else not open

        self.relay.set_relay_state(valve_state)
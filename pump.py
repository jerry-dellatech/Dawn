from single_relay import SingleRelay

"""Vacuum pump controller"""

class VacuumPump:
    # consts for readability
    ON = True
    OFF = False

    def __init__(self, relay:SingleRelay, state=OFF):
        self.relay = relay
        self.set_pump(state)

    @property
    def state(self) -> bool:
        return self.relay.get_relay_state()

    def set_pump(self, state: bool):
        self.relay.set_relay_state(state)
from relay import Relay

"""Vacuum pump controller"""

class VacuumPump:
    # consts for readability
    ON = True
    OFF = False

    def __init__(self, relay_controller, connected_relay:int, state=OFF):
        self.relay_controller: Relay = relay_controller
        self.connected_relay = connected_relay
        self.state = state
        self.set_pump(state)

    def set_pump(self, state: bool):
        self.relay_controller.set_relay_state(self.connected_relay, state)
        self.state = state
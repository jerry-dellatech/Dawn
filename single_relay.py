from relay import Relay

"""Defines SingleRelay to deal with individual relays on relay board with cleaner syntax."""

class SingleRelay:
    def __init__(self, relay_controller:Relay, relay_number:int):
        self.relay_controller = relay_controller
        self.relay_number = relay_number

    def set_relay_state(self, state:bool) -> None:
        self.relay_controller.set_relay_state(self.relay_number, state)

    def set_relay_off(self) -> None:
        self.set_relay_state(False)

    def set_relay_on(self) -> None:
        self.set_relay_state(True)

    def get_relay_state(self) -> bool:
        return self.relay_controller.get_relay_state(self.relay_number)
    
    @property
    def state(self) -> bool:
        return self.get_relay_state()
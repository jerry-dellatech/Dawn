from machine import Pin
import qwiic_i2c
import relay

"""Defines pin constants"""

class GPIOPin(Pin):
    """Makes defining I2C drivers easier"""
    def __init__(self, num:int, mode:int, pull=Pin.PULL_DOWN, *args, **kwargs):
        self.pin_number, self.pin_mode, self.pull = num, mode, pull
        super().__init__(num, mode, pull, *args, **kwargs)

# needed for boards without integrated QWIIC port
# SCL = GPIOPin(17, Pin.OUT)
# SDA = GPIOPin(16, Pin.OUT)

I2C_DRIVER = qwiic_i2c.get_i2c_driver()# sda=SDA.pin_number, scl=SCL.pin_number)

RELAY_CONTROLLER = relay.Relay(0x6D)#, I2C_DRIVER) # 6D is default address

START = GPIOPin(15, Pin.IN, Pin.PULL_DOWN)
STOP = GPIOPin(14, Pin.IN, Pin.PULL_DOWN)
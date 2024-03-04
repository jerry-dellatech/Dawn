import qwiic_relay
from machine import Pin, I2C, RTC
from time import sleep
import sys

# i2c = I2C(0,scl=Pin(17),sda=Pin(16),freq=100000)
# print(i2c.scan())

def time_str(now):
    ''' Return formatted time string for form mm/dd/yy hh:mm:ss. '''
    return f'{now[1]}/{now[2]}/{now[0]} {now[4]}:{now[5]}:{now[6]}'

def print_relay_status(relays):
    # Print the status of all relays
    print(f'Relay 1 state: {relays.get_relay_state(1)}')
    print(f'Relay 2 state: {relays.get_relay_state(2)}')
    print(f'Relay 3 state: {relays.get_relay_state(3)}')
    print(f'Relay 4 state: {relays.get_relay_state(4)}')
    print()

# set the real time clock (RTC)
rtc = RTC()
timestr = input('Input current datetime: YYYY,MM,DD,HH,MM (0 for no change): ')
if timestr != '0':
    datetime_list = [int(s) for s in timestr[1:-1].split(',')]
    rtc.datetime(tuple(datetime_list))
now = rtc.datetime()
print(time_str(now))

# print(f'creating relay...')
relays = qwiic_relay.QwiicRelay(qwiic_relay.QUAD_RELAY_DEFUALT_ADDR)

if relays.begin() == False:
    print("The Qwiic Relay isn't connected to the system. Please check your connection")
    sys.exit()

# Turn on relays one and three
relays.set_relay_on(1)
relays.set_relay_on(3)

print_relay_status(relays)

sleep(5)

relays.set_all_relays_off()

# Print the status of all relays
now = rtc.datetime()
print(time_str(now))
print(f'Relay 1 state: {relays.get_relay_state(1)}')
print(f'Relay 2 state: {relays.get_relay_state(2)}')
print(f'Relay 3 state: {relays.get_relay_state(3)}')
print(f'Relay 4 state: {relays.get_relay_state(4)}')
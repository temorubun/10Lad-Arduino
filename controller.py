import pyfirmata
import time

comport = 'COM11'
board = pyfirmata.Arduino(comport)
time.sleep(2)  # Allow time for the connection to be established

# Define LED pins
led_pins = {
    1: board.get_pin('d:2:o'),
    2: board.get_pin('d:3:o'),
    3: board.get_pin('d:4:o'),
    4: board.get_pin('d:5:o'),
    5: board.get_pin('d:6:o'),
    6: board.get_pin('d:7:o'),
    7: board.get_pin('d:8:o'),
    8: board.get_pin('d:9:o'),
    9: board.get_pin('d:10:o'),
    10: board.get_pin('d:11:o')
}

def led(fingerUp):
    num_fingers = sum(fingerUp)
    board.digital[13].write(1)  # Signal start of transmission
    time.sleep(0.1)
    board.digital[13].write(0)
    time.sleep(0.1)
    board.digital[13].write(1)
    time.sleep(0.1)
    board.digital[13].write(0)
    time.sleep(0.1)
    
    board.send_sysex(pyfirmata.STRING_DATA, bytearray(str(num_fingers), 'utf-8'))

#!/usr/bin/env python
from time import sleep
from random import randrange as rand, randint
from threading import Thread
import sys


def getdevpath():
    # NOTE: This only finds the first device. (Should only be one per device.) 
    for i in range(10):
        with open('/sys/class/hidraw/hidraw'+str(i)+'/device/uevent') as file:
            if 'Microchip Technology Inc. Composite HID + CDC, APP-ESS14-1' in file.read():
#                print('found at /dev/hidraw' +str(i))
                return '/dev/hidraw'+str(i)
#            else:
#                print('not found at /dev/hidraw' + str(i)) 
    return None

colors = {
        'red': 0x01,
        'green': 0x02,
        'blue': 0x03,
        'cyan': 0x06,
        'magenta': 0x05,
        'yellow': 0x04,
        'black': 0x08,
        'white': 0x07
        }

chsum = lambda b0, b1, b3: (21*b0**2 + 19*b1 - 3*b3) % 255

def bg(f, *args):
    t = Thread(target=f, args=args)
    t.start()

def turn_on(color='white',delay=0.0,override=-1):
    cmd = bytearray.fromhex('ff'*64)
    cmd[0] = 0x11
    if override != -1:
        cmd[1] = override
    else:
        cmd[1] = colors[color]
    cmd[3] = rand(255)
    cmd[2] = chsum(cmd[0], cmd[1], cmd[3])
    devpath = getdevpath()
    with open(devpath, 'wb') as device:
        device.write(cmd)
    sleep(delay)

def turn_off(delay=0.0):
    turn_on('black',delay)

def blink(color, count=1, delay=0.2):
    for i in range(count):
        print("Color: " + color)
        turn_on(color, delay)
        turn_off(delay)
    turn_off()

def gay(count=1):
    count=int(count)
    for j in range(count):
        for i,c in enumerate(['red','green','blue','cyan','magenta','yellow']):
            #print("Color: " + c)
            turn_on(color=c,delay=0.1)
        turn_off(delay=0.2)
    turn_off(delay=1)


def trans(count=1):
    count=int(count)
    for j in range(count):
        for i,c in enumerate(['cyan', 'magenta', 'white', 'magenta', 'cyan']):
            print("Color: " + c)
            turn_on(color=c,delay=0.1)
        turn_off(delay=0.2)
    turn_off(delay=1)


def ace(count=1):
    count=int(count)
    for j in range(count):
        for i,c in enumerate(['black', 'gray', 'white', 'white', 'purple']):
            print("Color: " + c)
            if c == 'gray':
                for x in range(5):
                    if x % 2 == 0:
                        turn_on(color='black', delay=0.02)
                    else:
                        turn_on(color='white', delay=0.02)
            elif c == 'purple':
                for x in range(5):
                    if x % 2 == 0:
                        turn_on(color='blue', delay=0.02)
                    else:
                        turn_on(color='magenta', delay=0.02)
            else:
                turn_on(color=c,delay=0.1)
        turn_off(delay=0.2)
    turn_off(delay=1)

 
def nb(count=1):
    count=int(count)
    for j in range(count):
        for i,c in enumerate(['yellow', 'white', 'magenta', 'black']):
            print("Color: " + c)
            turn_on(color=c,delay=0.1)
        turn_off(delay=0.2)
    turn_off(delay=1)

def bi(count=1):
    count=int(count)
    for j in range(count):
        for i,c in enumerate(['magenta', 'magenta', 'purple', 'blue', 'blue']):
            print("Color: " + c)
            if c == 'purple':
                for x in range(5):
                    if x % 2 == 0:
                        turn_on(color='blue', delay=0.02)
                    else:
                        turn_on(color='magenta', delay=0.02)
            else:
                turn_on(color=c,delay=0.1)
        turn_off(delay=0.2)
    turn_off(delay=1)




def randomness():
    turn_on(color='white',delay=0.1, override = randint(1,7))
#    for i,c in enumerate(['red','green','blue','cyan','magenta','yellow','white']):
#        turn_on(c,0.1)
#    turn_off(0.2)

if __name__=='__main__':
    try: 
        col, cnt = sys.argv[1:3]
        if col == 'gay' or col == 'rainbow':
            gay(count=int(cnt))
        elif col == 'trans':
            trans(count=int(cnt))
        elif col == 'ace':
            ace(count=int(cnt))
        elif col == 'nb':
            nb(count=int(cnt))
        elif col == 'bi':
            bi(count=int(cnt))
        elif col == "<3":
            gay(count=int(cnt))
            blink('black', count=1, delay=0.5);
            trans(count=int(cnt))
            blink('black', count=1, delay=0.5);
            ace(count=int(cnt))
            blink('black', count=1, delay=0.5);
            nb(count=int(cnt))
            blink('black', count=1, delay=0.5);
            bi(count=int(cnt))
            blink('black', count=1, delay=0.5);
        else:
            bg(blink, col, int(cnt))
    except: 
        print('Defaulting to randomness')
        while(True):
            #gay()
            randomness()
#    except:bg(blink, "white")

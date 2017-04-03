#!/usr/bin/env python

import signal
import time
import sys
import serial

from pirc522 import RFID

run = True
rdr = RFID()
util = rdr.util()
util.debug = False

def end_read(signal,frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()
    sys.exit()

signal.signal(signal.SIGINT, end_read)

print("Starting")
while run:
    rdr.wait_for_tag()

    (error, data) = rdr.request()
    if not error:
        print("\nDetected: " + format(data, "02x"))

    (error, uid) = rdr.anticoll()
    if not error:
        print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
        tag = ",".join([str(x) for x in uid[:-1]])
        #print(tag)
        timeout = time.time() + 60*1 #1 min While
        while True:
          barcode = 0
          barcode = input("Scan Barcode: ")
          if barcode != 0 or time.time() > timeout:
            #print(barcode)
            break

        """
        print("Setting tag")
        util.set_tag(uid)

        print("\nAuthorizing")
        #util.auth(rdr.auth_a, [0x12, 0x34, 0x56, 0x78, 0x96, 0x92])
        util.auth(rdr.auth_b, [0x74, 0x00, 0x52, 0x35, 0x00, 0xFF])
        print("\nReading")
        util.read_out(4)
        print("\nDeauthorizing")
        util.deauth()
        """

        time.sleep(1)

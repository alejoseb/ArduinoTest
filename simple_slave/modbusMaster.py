#!/usr/bin/env python3
# scripts/example/simple_rtu_client.py
#'/dev/cu.wchusbserial142340', baudrate=19200, parity=PARITY_NONE,
import minimalmodbus
import time
#i=minimalmodbus.Instrument('/dev/cu.wchusbserial142340',1)
#i=minimalmodbus.Instrument('/dev/cu.usbmodem14243',1)
i=minimalmodbus.Instrument('/dev/cu.usbmodem142323',1)
#i=minimalmodbus.Instrument('/dev/cu.usbserial-A50285BI',1)
i.serial.baudrate=19200

time.sleep(1)

i.debug=True
i.serial.timeout=1

while(True):
   a=i.read_registers(0,5)
   print(a)
   time.sleep(2)
   
   
  
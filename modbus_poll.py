# -*- coding: utf-8 -*-
"""Minimal Modbus RTU poll sample for an HCK cabinet air conditioner.

Install:  pip install pymodbus
Wiring:   AC RS485 A/B -> USB-RS485 dongle; set unit ID on the AC (default 1).
NOTE:     Register addresses below are EXAMPLES — verify against the model manual.
"""
from pymodbus.client import ModbusSerialClient


PORT = "COM3"          # Linux: "/dev/ttyUSB0"
UNIT_ID = 1
BAUDRATE = 9600


def main():
    client = ModbusSerialClient(port=PORT, baudrate=BAUDRATE, parity="N", stopbits=1, timeout=2)
    if not client.connect():
        raise SystemExit("cannot open %s" % PORT)

    # 0x0001 return-air temp, 0x0002 setpoint, 0x0003 run, 0x0004 alarm, 0x0005 fault
    rr = client.read_holding_registers(address=0x0001, count=5, slave=UNIT_ID)
    if rr.is_error():
        raise SystemExit("read error: %s" % rr)

    ret_temp, setpoint, run, alarm, fault = rr.registers
    print("return-air temp : %.1f C" % (ret_temp / 10.0))
    print("setpoint        : %.1f C" % (setpoint / 10.0))
    print("running         : %s" % ("yes" if run & 0x01 else "no"))
    print("alarm           : %s" % ("ACTIVE" if alarm else "none"))
    print("fault code      : %d" % fault)

    client.close()


if __name__ == "__main__":
    main()

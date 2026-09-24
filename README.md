# HCK Cabinet Air Conditioner — RS485 / Modbus Integration

An example Modbus RTU (RS485) register map and a minimal Python poll sample for monitoring HCK
cabinet air conditioners. Use it to read temperature, run status and alarms into a BMS / SCADA.

## Typical register map (example — verify against the model manual)
| Address | Name | Type | Access | Notes |
|---|---|---|---|---|
| 0x0001 | Return-air temperature | int16 (×0.1 °C) | read | e.g. 325 = 32.5 °C |
| 0x0002 | Setpoint temperature | int16 (×0.1 °C) | read / write | control target |
| 0x0003 | Run status | uint16 | read | bit0 = running |
| 0x0004 | Alarm status | uint16 | read | 0 = normal |
| 0x0005 | Fault code | uint16 | read | 0 = no fault |

Baud rate is typically 9600, 8N1; unit ID is set on the AC (default often 1).

## Sample
See `modbus_poll.py` in this repo (minimal, using `pymodbus`).

## Resources
- [Product range](https://www.zjhcc.com/en/products.html)
- [Technical white paper](https://www.zjhcc.com/en/whitepaper.html)
- [Official site](https://www.zjhcc.com/en/)

*Zhejiang Haocheng Industrial Control Equipment Co., Ltd. · HCK Cabinet Air Conditioners · IP55 · −40…+55 °C · R410A · rotary compressor · RS485 · CE-marked · OEM/ODM*

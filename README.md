Web-based LED strip control with Raspberry Pi. Requires pigpio.

```
 _________
|         |
|         |        ___________________         ___________
|        17-------|                   |-------|           |
|  RPi   27-------|   3V3 - 5V        |-------| 3xIRF3205 |
|        22-------|   level shifter   |-------|___________|
|         |       |___________________|
|         |
|_________|

```

- red\_pin = 17
- green\_pin = 27
- blue\_pin = 22

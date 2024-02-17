Web-based LED strip control with Raspberry Pi. Requires pigpio.

```
 _________
|         |
|         |        ________________________         ___________
|        17-------|                        |-------|           |
|  RPi   27-------| 3V3 - 5V bidirecional  |-------| 3xIRF3205 |
|        22-------| level shifter          |-------|___________|
|         |       |________________________|
|         |
|_________|

```

red_pin = 17
green_pin = 27
blue_pin = 22

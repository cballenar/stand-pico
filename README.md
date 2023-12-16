# Stand Pico
Time to stand alert system built with Raspberry Pi Pico and seat sensor.

![Photo of basic setup](https://raw.githubusercontent.com/cballenar/stand-pico/main/stand-pico.jpg)

## How it works
Sitting time will be counted as if it were a glass of water. The more you sit, the more it fills up (1 per second). Time standing will subtract from it at a faster rate (4 per second). This will result in 1hr being cleared with 15mins of standing.

As time increases, LEDs will light up from 0 to 4 when you've been sitting for over an hour.

The idea is for the next version to send a notification to Homekit/Homebridge to alert you to stand up.

## Parts Used
- Raspberry Pi Pico
- Seat Sensor: [XINJIEJIA SBR JYJ-105](http://en.szxjj.com/index.php?m=content&c=index&a=show&catid=13&id=3) (Via Amazon)
- Breadboard, LEDs, resistors, wires

## Sources
- https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf
- https://www.instructables.com/LDR-Light-Sensor-on-Raspberry-Pi-Pico/
- https://www.youtube.com/watch?v=L46n-8-GCHQ
- https://www.dcode.fr/function-equation-finder
- ChatGPT?

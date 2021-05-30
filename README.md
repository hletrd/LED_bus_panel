# LED bus panel
* 서울 버스 전광판 제작용 파일
* 제작과정: [https://atik.kr/2021/05/bus-panel/](https://atik.kr/2021/05/bus-panel/)

![예시](example.jpg)

---

## Bill of materials
### Parts
* 6 * P4 RGB LED panels (64x32)
* A Raspberry Pi 4
* [Adafruit RGB matrix HAT](https://www.adafruit.com/product/2345)
* 5V, >150W SMPS

### Materials, with some workings
* 5mm MDF (to make the frame)
  * 레이저 커터로 절단해서 프레임을 제작함
* 3D printer (to make the stand)
  * 3D 프린터로 받침대를 출력함
* Power distribution PCB

### Miscs
* M3 bolts / nuts (to assemble the frames and stands)
  * M3 10mm, 15mm, 20mm bolts
  * M3 nuts
* Wirings (for power supply)
  * JST VH 3.96mm 4P connector, and wirings
* Wirings (for HUB75 connection)
  * 2x10pin 2.54mm IDC cables

---

## Python library

### Requirements
* [Python 3](https://python.org/)
* Install [PIL](https://pillow.readthedocs.io/en/stable/), [NumPy](https://numpy.org/)
* Install [RPi RGB LED matrix](https://github.com/hzeller/rpi-rgb-led-matrix) with its Python bindings.
* Put the library files in ```/python/library/``` directory into the project folder, or install the module system-wide.

### Running the examples
* Run sample scripts in ```/python/example/``` directory with ```sudo```.

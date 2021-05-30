import bus
import xylopanel

buspanel = bus.BusPanel()
panel = xylopanel.Panel()

buspanel.clear()
panel.clear()

buspanel.add_bus('5511', time=10, lowdeck=True) #저상버스
buspanel.add_bus('5513', time=15)
buspanel.add_bus('5511', time=xylopanel.BusPanel.end) #종료
buspanel.add_bus('5516', time=xylopanel.BusPanel.depot) #차고지

buspanel.add_arrive('750A', density=2) #곧도착, 혼잡
buspanel.add_arrive('750B', density=1) #곧도착, 보통
buspanel.add_arrive('506', density=0) #곧도착, 여유

img = buspanel.get_image() #Pillow 이미지를 만들어서 가져옴
panel.draw_image((0, 0), img) #LED 패널 객체에 이미지를 그림
panel.send() #LED 패널로 이미지 전송

import time
time.sleep(100)

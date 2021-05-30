import bus
import xylopanel

buspanel = bus.BusPanel()
panel = xylopanel.Panel()

buspanel.clear()
panel.clear()

buspanel.add_bus('5511', time=10, lowdeck=True)
buspanel.add_bus('5513', time=15)
buspanel.add_bus('5511', time=xylopanel.BusPanel.end)
buspanel.add_bus('5516', time=xylopanel.BusPanel.depot)

buspanel.add_arrive('750A', density=2)

img = buspanel.get_image()
panel.draw_image((0, 0), img)
panel.send()


import time
time.sleep(100)

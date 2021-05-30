try:
	from PIL import Image, ImageFont, ImageDraw
except:
	sys.stderr.write('Pillow is not installed.\n')

try:
	import numpy as np
except:
	sys.stderr.write('NumPy is not installed.\n')
import os

class BusPanel:
	black = (0, 0, 0)
	white = (255, 255, 255)
	red = (255, 0, 0)
	green = (0, 255, 0)
	blue = (0, 0, 255)
	orange = (255, 128, 0)
	yellow = (255, 255, 0)
	magenta = (255, 0, 255)
	cyan = (0, 255, 255)

	end = -2
	depot = -3

	@staticmethod
	def load_font():
		cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		bus = Image.open(os.path.join(cwd, 'font.png'))
		with open(os.path.join(cwd, 'font.txt'), 'r') as f:
			bus_str = f.readline()
		bus_img = {}

		bus_arr = np.array(bus, dtype=np.uint8)
		bus_arr = bus_arr // 255
		bus_arr_size = bus_arr.shape
		start = 0
		count = 0
		for i in range(bus_arr_size[1]):
			if bus_arr[bus_arr_size[0]-1,i] == 1:
				bus_img[bus_str[count:count+1]] = bus_arr[:15,start:i+1]
				start = i + 1
				count = count + 1
		return bus_img

	@staticmethod
	def get_text_width(text, font):
		width = 0
		for i in text:
			if i in font:
				char = font[i]
				width += char.shape[1]
				width += 1
			else:
				continue
		return width

	def print_text(self, text, font, color, xy, align='left'):
		x = xy[0]
		y = xy[1]

		if align == 'right':
			width = self.get_text_width(text, self.font)
			x -= width

		for i in text:
			if i in font:
				char = font[i]
				char_size = char.shape
				char_img = Image.fromarray(char*255)
				self.draw.bitmap((x, y), char_img, fill=color)
				x += char_size[1]+1

	def __init__(self):
		self.img = Image.new("RGB", (192, 64), self.black)
		self.draw = ImageDraw.Draw(self.img)
		self.font = self.load_font()

		self.draw.line([(96, 0), (96, 48)], self.yellow)
		self.draw.rectangle([(0, 48), (191, 63)], outline=self.yellow)
		self.print_text('곧도착:', self.font, self.white, (2, 49))

		self.arrive_start = 42
		self.arrive_x = self.arrive_start
		self.bus_count = 0
		self.arrive_first = True

	def add_bus(self, line, time=0, lowdeck=False):
		row = self.bus_count % 3
		column = self.bus_count // 3
		y = row * 16
		if column == 0:
			x = 3
		elif column == 1:
			x = 99
		if time >= 0:
			time_str = '{}분'.format(time)
			time_color = self.cyan
		elif time == self.end:
			time_str = '종료'
			time_color = self.red
		elif time == self.depot:
			time_str = '차고지'
			time_color = self.orange

		offset = 0
		for i in line:
			if i in '0123456789':
				color = self.white
			else:
				color = self.cyan
			self.print_text(str(i), self.font, color, (x+offset, y))
			offset += self.get_text_width(str(i), self.font)
			
		self.print_text('저상' if lowdeck else '', self.font, self.green, (x+40, y))
		self.print_text(time_str, self.font, time_color, (x+93, y), align='right')
		self.bus_count += 1

	def set_arrive_position(self, x=0):
		self.arrive_x = self.arrive_start - x
		self.arrive_first = True

	def get_arrive_len(self):
		return self.arrive_x - 190

	def init_arrive(self):
		self.arrive_first = True
		self.draw.rectangle([(0, 48), (191, 63)], outline=self.yellow, fill=self.black)
		self.print_text('곧도착:', self.font, self.white, (2, 49))

	def add_arrive(self, line, density=0):
		y = 49
		if density == 0:
			density_text = '여유'
			density_color = self.green
		elif density == 1:
			density_text = '보통'
			density_color = self.orange
		elif density == 2:
			density_text = '혼잡'
			density_color = self.red
		if self.arrive_first == True:
			self.arrive_first = False
		else:
			self.print_text(',', self.font, self.white, (self.arrive_x, y))
			self.arrive_x += self.get_text_width(',', self.font)
		self.print_text(str(line), self.font, self.white, (self.arrive_x, y))
		self.arrive_x += self.get_text_width(str(line), self.font)

		self.arrive_x += 0
		self.print_text('(', self.font, self.yellow, (self.arrive_x, y))
		self.arrive_x += self.get_text_width('(', self.font)
		self.print_text(density_text, self.font, density_color, (self.arrive_x, y))
		self.arrive_x += self.get_text_width(density_text, self.font)
		self.print_text(')', self.font, self.yellow, (self.arrive_x, y))
		self.arrive_x += self.get_text_width(')', self.font)

		self.arrive_x -= 3
		self.draw.rectangle([(0, 48), (191, 63)], outline=self.yellow)
		nextarrive = self.get_text_width('곧도착:', self.font)
		self.draw.rectangle([(1, 49), (nextarrive, 62)], fill=self.black)
		self.print_text('곧도착:', self.font, self.white, (2, 49))

	def clear(self):
		self.img = Image.new("RGB", (192, 64), self.black)
		self.draw = ImageDraw.Draw(self.img)

		self.draw.line([(96, 0), (96, 48)], self.yellow)
		self.draw.rectangle([(0, 48), (191, 63)], outline=self.yellow)
		self.print_text('곧도착:', self.font, self.white, (1, 49))

		self.arrive_x = self.arrive_start
		self.bus_count = 0


	def get_image(self):
		return self.img


import sys

try:
	from PIL import Image, ImageFont, ImageDraw
except:
	sys.stderr.write('Pillow is not installed.\n')

import colorsys
import random
try:
	import numpy as np
except:
	sys.stderr.write('NumPy is not installed.\n')

try:
	from rgbmatrix import RGBMatrix, RGBMatrixOptions
except:
	sys.stderr.write('RGBMatrix library is not installed.\n')

class colors:
	black = (0, 0, 0)
	white = (255, 255, 255)
	red = (255, 0, 0)
	green = (0, 255, 0)
	blue = (0, 0, 255)
	orange = (255, 128, 0)
	yellow = (255, 255, 0)
	magenta = (255, 0, 255)
	cyan = (0, 255, 255)

	@staticmethod
	def random_color():
		rndcolor = colorsys.hsv_to_rgb(random.random(), 0.6, 1)
		rndcolor = tuple(map(lambda x: int(x*256), rndcolor))
		return rndcolor

class Panel:
	width = 192
	height = 64

	@staticmethod
	def load_font(fontfile, point=16):
		font = ImageFont.truetype(fontfile, point)
		return font

	@staticmethod
	def load_image(imagefile, size=(192, 64)):
		img = Image.open(imagefile)
		img.thumbnail((size[0], size[1]))
		return img

	def __init__(self):
		try:
			self.options = RGBMatrixOptions()
			self.options.rows = 32
			self.options.cols = 64
			self.options.chain_length = 6
			self.options.parallel = 1
			self.options.hardware_mapping = 'adafruit-hat-pwm'
			self.options.gpio_slowdown = 1

			self.options.pwm_lsb_nanoseconds = 130
			self.options.pwm_bits = 11

			self.matrix = RGBMatrix(options=self.options)
			self.matrix.brightness = 100

			self.image = Image.new("RGB", (self.width, self.height), colors.black)
			self.draw = ImageDraw.Draw(self.image)
		except Exception as e:
			sys.stderr.write('Failed to initialize.\n')
			sys.stderr.write(str(e))

	def set_brightness(self, brightness):
		self.matrix.brightness = brightness

	def clear(self):
		self.image = Image.new("RGB", (self.width, self.height), colors.black)
		self.draw = ImageDraw.Draw(self.image)

	def fill(self, color=(0, 0, 0)):
		self.draw.rectangle((0, 0, self.width, self.height), fill=color)

	def send(self):
		output = Image.new("RGB", (384, 32))
		output.paste(self.image.crop((0, 0, 192, 32)), (192, 0))
		output.paste(self.image.crop((0, 32, 192, 64)).rotate(180), (0, 0))
		self.matrix.SetImage(output)

	def draw_text(self, xy, string, font, color):
		self.draw.text(xy, string, font=font, fill=color)
		text_size = font.getsize(string)
		return text_size

	def draw_image(self, xy, image):
		self.image.paste(image, xy)

	def draw_rectangle(self, xy, fill=None, outline=None, width=1):
		self.draw.rectangle(xy, fill, outline, width)

	def draw_pixel(self, xy, color):
		self.draw.point(xy, fill=color)

	def get_image(self):
		return self.image

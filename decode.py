from PIL import Image
import binascii
from stega_help import *

def decode(filename):
	"""
	Highest level function used to decode the image
	and extract the message. The image is passed in with
	the parameter filename. The message length is encoded
	with the first 3 pixels.  Each pixel afterwards holds
	3 bits of information represented in R, G, and B.
	If the RGB is even, the bit is 0.  Odd represents 1.
	"""
	img = Image.open(filename)
	dims = img.size
	y_pixels = img.size[1]
	x_pixels = img.size[0]
	len_bin = ''
	# Get length
	for j in range(y_pixels):
		for i in range(x_pixels):
			if j == 0 and i < 3:
				r, g, b = img.getpixel((i, j))
				len_bin += high_or_low(r)
				len_bin += high_or_low(g)
				len_bin += high_or_low(b)
			else:
				break
	msg_len = int(len_bin, 2)
	msg_bin = ''
	count = msg_len * 8
	# Get message
	for j in range(y_pixels):
		for i in range(x_pixels):
			if j == 0 and i < 3:
				continue
			r, g, b = img.getpixel((i, j))
			if count == 0:
				break
			msg_bin += high_or_low(r)
			count -= 1
			if count == 0:
				break
			msg_bin += high_or_low(g)
			count -= 1
			if count == 0:
				break
			msg_bin += high_or_low(b)
			count -= 1
	msg = bin_to_ascii(msg_bin)
	print 'Hidden Message:\n', msg

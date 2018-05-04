from PIL import Image
import binascii
from stega_help import *

def encode(img_file, txt_file, dest_file):
	"""
	Embed the message within the image through this function.
	txt_file holds the txt that will be encoded. img_file
	holds the filename for the image that will hold the message.

	The message length is encoded in the first 3 pixels.

	The message with the hidden message is called the original filename
	with _hidden appended.  The image created is a PNG.
	"""
	msg, msg_len = get_msg(txt_file)
	#print msg
	bin_text = str_to_bin(msg, msg_len)
	#print bin_text, len(bin_text)
	#img = Image.open(img_file)
	img = evenize(img_file)
	dims = img.size
	hidden_img = Image.new('RGB', dims)
	y_pixels = img.size[1]
	x_pixels = img.size[0]
	count = len(bin_text)
	if msg_len >= 256:
		raise ValueError("The message length exceeds 255 characters. \
There are currently " + str(msg_len) + " characters." )
	if count >= (y_pixels * x_pixels * 3):
		raise ValueError("The message length is too big for the image. \
Either use a bigger image or shorten the message.")
	# Each pixel stores 3 bits
	for j in range(y_pixels):
		for i in range(x_pixels):
			flat_pix_num = j*x_pixels + i
			# Because there are 3 hidden bits in each pixel (RGB)
			slice_begin = flat_pix_num * 3
			slice = bin_text[slice_begin:slice_begin+3]
			#print flat_pix_num, slice_begin, slice
			r, g, b = img.getpixel((i, j))
			# Will sometimes end mid-pixel
			if count > 0:
				new_r = r + int(slice[0])
				count -= 1
			else:
				new_r = r
			if count > 0:
		   		new_g = g + int(slice[1])
		   		count -= 1
			else:
				new_g = g
			if count > 0:
		   		new_b = b + int(slice[2])
		   		count -= 1
			else:
				new_b = b
			hidden_img.putpixel((i, j), (new_r, new_g, new_b))
	hidden_img.save(dest_file, 'PNG')

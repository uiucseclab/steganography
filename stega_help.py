from PIL import Image
import binascii

def even_pix(channel):
	"""
	change channel to an even number
	"""
	if channel % 2 != 0:
		if channel < 255:
			channel += 1
		else:
			channel -= 1
	return channel

def evenize(filename):
	"""
	Open file and get RGB values.  Change all RGB to even values
	and save into a new image.
	"""
	img = Image.open(filename)
	#mg.convert('RGB')
	dims = img.size
	even_img = Image.new('RGB', dims)
	y_pixels = img.size[1]
	x_pixels = img.size[0]
	for j in range(y_pixels):
		for i in range(x_pixels):
			r, g, b = img.getpixel((i, j))
			new_r = even_pix(r)
			new_g = even_pix(g)
			new_b = even_pix(b)
			#new_a = even_pix(a)
			#even_img.putpixel((i, j), (new_r, new_g, new_b, new_a))
			even_img.putpixel((i, j), (new_r, new_g, new_b))
	#new_filename = filename[:-4] + '_even.png'
	#even_img.save(new_filename, 'PNG')
	return even_img

def get_msg(filename):
	"""
	Open file and extract the message.  Return message
	"""
	file = open(filename, 'r')
	msg = ''
	for line in file:
		msg += line
	return msg, len(msg)-1

def str_to_bin(msg, msg_len):
	"""
	return the text message as a binary
	"""
	bin_str = ''
	bin_msg_len = bin(msg_len)
	bml_stripped = bin_msg_len[2:]
	# Zero-pad length to 8 bits
	while len(bml_stripped) < 9:
		bml_stripped = '0' + bml_stripped
	bin_str += bml_stripped
	for char in msg[:-1]:
		bin_val = bin(ord(char))
		#print 'Binary:', bin_val, 'for char:', char
		# Get rid of '0b' part
		stripped = bin_val[2:]
		while len(stripped) < 8:
			stripped = '0' + stripped
		bin_str += stripped
	return bin_str


def high_or_low(channel):
	"""
	Determine if the channel represents 0 or 1.
	"""
	if channel % 2 == 0:
		return '0'
	else:
		return '1'

def bin_to_ascii(msg_bin):
	"""
	Convert binary string to ascii
	"""
	#print 'Bits in message', len(msg_bin)
	msg = ''
	ascii_str = ''
	for bit in msg_bin:
		ascii_str += bit
		if len(ascii_str) == 8:
			ascii_int = int(ascii_str, 2)
			#print ascii_int
			msg_char = chr(ascii_int)
			msg += msg_char
			ascii_str = ''
	return msg

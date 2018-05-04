#!/usr/bin/env python

from PIL import Image
import binascii
from decode import decode
from encode import encode
from sendEmail import sendEmail

"""
steganography.py
Does all the steganography functions to manipulate the image.
Encodes and decodes the messgages to return to the user.
"""

def main():
	user_input = int(raw_input("Welcome \
to steganography.\nEnter 1 for encoding \
an image or 2 for decoding an image.\n"))
	if user_input == 1:
		print "Message length must have a length less than 255."
		encode_image = raw_input("Please enter the \
image you would like to encode your message \
into.\n")
		hidden_text = raw_input("Please enter the \
text file that contains the message you \
would like to send.\n")
		dest_image = raw_input("Please enter the \
filename you would like the encoded image \
to be called.\n")
		encode(encode_image, hidden_text, dest_image)
		user_email = int(raw_input("Would you like to send this in an email?\n\
If so, enter 1. If not, enter any other character.\n"))
		if user_email == 1:
			sendEmail(dest_image);
	elif user_input == 2:
		decode_image = raw_input("Please enter the \
image you would like to decode.\n")
		decode(decode_image)
	else:
		print "You have entered an invalid option."


if __name__ == '__main__':
	main()

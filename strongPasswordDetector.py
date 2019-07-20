#! /usr/bin/python3

# Strong passward detection script

import re

print("Enter your password: \t")
password = input() 
matches = []


lowerRegex = re.compile(r'[a-z]')
upperRegex = re.compile(r'[A-Z]')
numRegex = re.compile(r'[0-9]')
passwordRegex = re.compile(r'[a-zA-Z0-9]')


if lowerRegex.findall(password) != []:
	if upperRegex.findall(password) != []:
		if numRegex.findall(password) != []:
			for letters in passwordRegex.findall(password):
				matches.append(letters)
if len(matches) >= 8:
	print('Strong passwords:')
	print(''.join(matches))
else:
	print('Not a strong password!')

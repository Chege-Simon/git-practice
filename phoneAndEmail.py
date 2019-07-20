#! /usr/bin/python3

# program that find phone numbers and emails in a text document

import pyperclip,re

text = str(pyperclip.paste())

phoneRegex = re.compile(r'''(
				("+254"|\d{3}|\d{4})
				(\s|-|\.)?
				(\d{3}|\d{4}|\d{2})
				(\s|-|\.)?
				(\d{7}|\d{4}|\d{3})
				)''', re.VERBOSE)

emailRegex = re.compile(r'''(
				[a-zA-Z0-9._%+-]+		# username
				@				# @ symbol
				[a-zA-Z0-9.-]+			# domain name
				(\.[a-zA-Z]{2,4})		# dot-something
				)''', re.VERBOSE)


matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if len(phoneNum) >= 12 and len(phoneNum) <= 14:
		matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')

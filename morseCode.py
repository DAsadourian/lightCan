#
def encodeMorse(a):	

	morseEncodeDictionary = {
		
		# Numbers
		'1': '. - - - -',
		'2': '. . - - -', 
		'3': '. . . - -',
		'4': '. . . . -',
		'5': '. . . . .',
		'6': '- . . . .',
		'7': '- - . . .',
		'8': '- - - . .',
		'9': '- - - - .',
		'0': '- - - - -',

		# Letters
		'a': '. -',
		'b': '- . . .',
		'c': '- . - .',
		'd': '- . .',
		'e': '.',
		'f': '. . - .',
		'g': '- - .',
		'h': '. . . .',
		'i': '. .',
		'j': '. - - -',
		'k': '- . -',
		'l': '. - . .',
		'm': '- -',
		'n': '- .',
		'o': '- - -',
		'p': '. - - .',
		'q': '- - . -',
		'r': '. - .',
		's': '. . .',
		't': '-',
		'u': '. . -',
		'v': '. . . -',
		'w': '. - -',
		'x': '- . . -',
		'y': '- . - -',
		'z': '- - . .',
	}

	a = a.lower()
	ignore = "`~!@#$%^&*()_+-=\\][|}{\';\":/.,?>< "
	encodedMorse = ""

	for letter in a:
		if letter in ignore:
			encodedMorse += ""
		else:
			encodedMorse += str(morseEncodeDictionary[letter] + " / ")

	return encodedMorse

#!
def decodeMorse(a):

	morseDecodeDictionary = {
		
		# Numbers
		'. - - - -': '1',
		'. . - - -': '2', 
		'. . . - -': '3',
		'. . . . -': '4',
		'. . . . .': '5',
		'- . . . .': '6',
		'- - . . .': '7',
		'- - - . .': '8',
		'- - - - .': '9',
		'- - - - -': '0',

		# Letters
		'. -': 'a',
		'- . . .': 'b',
		'- . - .': 'c',
		'- . .': 'd',
		'.': 'e',
		'. . - .': 'f',
		'- - .': 'g',
		'. . . .': 'h',
		'. .': 'i',
		'. - - -': 'j',
		'- . -': 'k',
		'. - . .': 'l',
		'- -': 'm',
		'- .': 'n',
		'- - -': 'o',
		'. - - .': 'p',
		'- - . -': 'q',
		'. - .': 'r',
		'. . .': 's',
		'-': 't',
		'. . -': 'u',
		'. . . -': 'v',
		'. - -': 'w',
		'- . . -': 'x',
		'- . - -': 'y',
		'- - . .': 'z'
	}

	morseCodeList = a.split(' / ')
	del morseCodeList[len(morseCodeList)-1]
	decodedMorse = ""

	for item in morseCodeList:
		decodedMorse += str(morseDecodeDictionary[item])

	return decodedMorse
# Light-Can

# Imports



def get_morse(message):
    '''
    '''
    
    message = message.lower()   

    morse_code = []

    morse_code_dictionary = {
        '1': '. - - - - /',
        '2': '. . - - - /',
        '3': '. . . - - /',
        '4': '. . . . - /',
        '5': '. . . . . /',
        '6': '- . . . . /',
        '7': '- - . . . /',
        '8': '- - - . . /',
        '9' : '- - - - . /',
        '0': '- - - - - /',
        'a': '. - /',
        'b': '- . . . /',
        'c': '- . - . /',
        'd': '- . . /',
        'e': '. /',
        'f': '. . - . /',
        'g': '- - . /',
        'h': '. . . . /',
        'i': '. . /',
        'j': '. - - - /',
        'k': '- . - /',
        'l': '. - . . /',
        'm': '- - /',
        'n': '- . /',
        'o': '- - - /',
        'p': '. - - . /',
        'q': '- - . - /',
        'r': '. - . /',
        's': '. . . /',
        't': '- /',
        'u': '. . - /',
        'v': '. . . - /',
        'w': '. - - /',
        'x': '- . . - /',
        'y': '- . - - /',
        'z': '- - . . /',
    }

    ignore = "`~!@#$%^&*()_+-=\\][|}{\';\":/.,?>< "

    for letter in message:
        if letter in ignore:
            morse_code += " "
        else:
            morse_code.append(morse_code_dictionary[letter])
    return morse_code


def main():
    user_input = input("Enter message: ")
    print(get_morse(user_input))


if __name__ == main():
    main()


# PEP-8 72 character ruler
# 1234567890123456789012345678901234567890123456789012345678901234567890

# PEP-8 79 character ruler
# 12345678901234567890123456789012345678901234567890123456789012345678901234567

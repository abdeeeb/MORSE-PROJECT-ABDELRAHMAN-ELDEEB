morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..',
                   '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                   ' ': ' '
                   }

def ecrpt_morse(text)
    text = text.upper()
    morse_code = []

    for char in text: 
        if char in morse_dict:
            morse_code.append(morse_dict[char])
        else: 
            morse_code.appd(' ')
    return ' '.join(morse_code)

def dcrypt_morse(morse):
    morse = morse.split(' ')
    text = ''

    reverse_morse_dict = {code: char for char, code inn morse_dict.items()}
    for symbol in morse:
        if symbol in reverse_morse_dict:
            text+= reverse_morse_dict[symbol]
        elif symbol == '/':
            text += ' '
        else:text += '#'
    return text

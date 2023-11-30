morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',                #The dictionary used to map out all the numbers and letters 
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..',
                   '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                   ' ': ' '
                   }

def ecrpt_morse(text):                               #defining the encryption function and making sure any input turns into uppercase letters
    text = text.upper()
    morse_code = []

    for char in text:                                #iterates through every charecter in the text to check if the charcter exists in the dictionary 
        if char in morse_dict:
            morse_code.append(morse_dict[char])
        else: 
            morse_code.append(' ')
    return ' '.join(morse_code)                      

def dcrypt_morse(morse):
    morse = morse.split(' ')
    text = ''

    reverse_morse_dict = {code: char for char, code in morse_dict.items()}
    for symbol in morse:
        if symbol in reverse_morse_dict:
            text+= reverse_morse_dict[symbol]
        elif symbol == '/':
            text += ' '
        else:text += '#'
    return text

def start_morse_app():
    print("THE MORSE CODE APP")
    while True: 
        user_choice = input("choose an action:\n'@' for encryption)\n'*' for decryption\n'%' to Exit\n").upper()

        if user_choice == '@':
            plaintext = input("enter the text to encrypt:")
            encrypted_text = ecrpt_morse(plaintext)
            print(f"encrypted text: {encrypted_text}\n")
        elif user_choice == '*':
            morse_code = input ("Enter morse code to decrypt (after every character add a space in between, for space in between words put a space after the last character then '/' then another space after '/'):")
            decrypted_text = dcrypt_morse(morse_code)
            print(f"decrypted text: {decrypted_text}\n")
        elif user_choice == '%':
            print("thank you. goodbye!")
            break
        else:
            print("Unknown option. Please choose '@' for Encryption, '*' for Decryption, or '%' to Exit.\n")

if __name__ == "__main__":
    start_morse_app()
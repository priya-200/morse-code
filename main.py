MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '_'}


def convert_to_morse_code(string):
    morse_code = ''
    for each in string:
        morse_code += f'{MORSE_CODE_DICT[each]} '
    return morse_code


def convert_to_sentence(string):
    sentence = ''
    strings = string.strip().split()
    for each in strings:
        for key, value in MORSE_CODE_DICT.items():
            if value == each:
                sentence += key
                break
    return sentence


if __name__ == '__main__':
    code = True
    while code:
        convert = input(
            'Print morse-code to convert the sentence to morse code or if you want to convert morse code into '
            'sentence print sentence : ').lower()
        if convert == 'morse-code':
            string = input("Enter the string that need to be converted to Morse code : ").upper()
            print(f'Your converted sentence :\n {convert_to_morse_code(string)}')
        elif convert == 'sentence':
            string = input('Enter the morse code that is to be converted : ')
            print(f'Your sentence is :\n {convert_to_sentence(string).lower()}')
        else:
            print('Invalid input try again ...')

import time
from adafruit_circuitplayground import cp

MORSE_CODE_DICT = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',
    'e': '.',     'f': '..-.',  'g': '--.',   'h': '....',
    'i': '..',    'j': '.---',  'k': '-.-',   'l': '.-..',
    'm': '--',    'n': '-.',    'o': '---',   'p': '.--.',
    'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
    'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',
    'y': '-.--',  'z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----',
}

def convert_to_morse(sentence):
    filtered_sentence = ''.join([ch for ch in sentence.lower() if ch in MORSE_CODE_DICT or ch == ' '])

    morse_code = []
    for word in filtered_sentence.split():
        morse_code.append(' '.join(MORSE_CODE_DICT[ch] for ch in word if ch in MORSE_CODE_DICT))
    return ' / '.join(morse_code)


def display_morse_on_cpx(morse_code, unit_time):
    for symbol in morse_code:
        if symbol == '.':
            cp.pixels.fill((0, 255, 0))
        elif symbol == '-':
            cp.pixels.fill((0, 255, 0))
            time.sleep(unit_time * 3)
        elif symbol == ' ':
            cp.pixels.fill((0, 0, 0))
            time.sleep(unit_time * 3)
        elif symbol == '/':
            cp.pixels.fill((0, 0, 0))
            time.sleep(unit_time * 7)
        cp.pixels.fill((0, 0, 0))
        time.sleep(unit_time)

def main():
    unit_time = float(input("input a unit time(0-1sec): "))
    sentence = input("input your sentence")
    morse_code = convert_to_morse(sentence)
    print("morse code: ", morse_code)
    display_morse_on_cpx(morse_code, unit_time)

if __name__ == "__main__":
    main()
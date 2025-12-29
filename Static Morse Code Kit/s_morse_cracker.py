import json

def decrypt(message, morse_code_dict):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(morse_code_dict.keys())[list(morse_code_dict.values()).index(citext)]
                citext = ''

    return decipher

def main():
    with open('Static Morse Code Kit/morse_code.json', 'r') as f:
        morse_code_dict = json.load(f)

    # Edit the message variable to the morse code you want to decrypt
    message = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    result = decrypt(message, morse_code_dict)
    print(result)

if __name__ == '__main__':
    main()
import json

def encrypt(message, morse_code_dict):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += morse_code_dict[letter.upper()] + ' '
        else:
            cipher += ' '

    return cipher

def main():
    with open('Static Morse Code Kit/morse_code.json', 'r') as f:
        morse_code_dict = json.load(f)

    # Edit the message variable to the text you want to encrypt
    message = "HELLO WORLD"
    result = encrypt(message.upper(), morse_code_dict)
    print(result)

if __name__ == '__main__':
    main()
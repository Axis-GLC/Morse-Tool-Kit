import json

def decrypt(message, morse_code_dict):
    message += ' '
    decipher = ''
    citext = ''
    morse_to_letter = {v: k for k, v in morse_code_dict.items()}

    for letter in message:
        if letter != ' ':
            citext += letter
        else:
            if citext:
                decipher += morse_to_letter.get(citext, '?')
                citext = ''
            else:
                decipher += ' '
    return decipher

def main():
    with open('Dynamic Morse Code Kit/morse_code.json', 'r') as f:
        morse_code_dict = json.load(f)

    while True:
        message = input("Enter a morse code to decrypt (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        result = decrypt(message, morse_code_dict)
        print(result)

if __name__ == '__main__':
    main()

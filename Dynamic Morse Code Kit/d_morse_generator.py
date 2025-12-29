import json

def encrypt(message, morse_code_dict):
    cipher = ''
    for letter in message.upper():
        if letter == ' ':
            cipher += ' '
        else:
            cipher += morse_code_dict.get(letter, '?') + ' '
    return cipher

def main():
    with open('Dynamic Morse Code Kit/morse_code.json', 'r') as f:
        morse_code_dict = json.load(f)

    while True:
        message = input("Enter a message to encrypt (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        result = encrypt(message, morse_code_dict)
        print(result)

if __name__ == '__main__':
    main()
.- .--- -.. -.. .. ... -.. .... .-. .. ..-. . .--
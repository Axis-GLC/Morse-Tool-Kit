# Dynamic Morse Code Kit

This folder contains a set of Python scripts for encrypting and decrypting morse code. This version of the kit is "dynamic", meaning the scripts will interactively ask you for the message you want to work with.

## How it Works

Both the generator and cracker scripts read the morse code dictionary from the `morse_code.json` file. The scripts then use this dictionary to perform the requested operation (encryption or decryption).

## How to Use

### d_morse_generator.py

To encrypt a message, run the script:

```
python "Dynamic Morse Code Kit/d_morse_generator.py"
```

The script will then prompt you to enter the message you want to encrypt. Type your message and press Enter. To quit the script, type `exit`.

### d_morse_cracker.py

To decrypt a message, run the script:

```javascript
python "Dynamic Morse Code Kit/d_morse_cracker.py"
```

The script will then prompt you to enter the morse code you want to decrypt. Type the morse code and press Enter. To quit the script, type `exit`.

## File Descriptions

- `morse_code.json`: A JSON file containing the morse code dictionary.
- `d_morse_generator.py`: A Python script to encrypt a message into morse code interactively.
- `d_morse_cracker.py`: A Python script to decrypt a morse code message interactively.

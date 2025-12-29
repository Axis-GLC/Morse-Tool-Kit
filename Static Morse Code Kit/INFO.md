# Static Morse Code Kit

This folder contains a set of Python scripts for encrypting and decrypting morse code. This version of the kit is "static", meaning you need to directly edit the Python files to change the message you want to work with.

## How it Works

Both the generator and cracker scripts read the morse code dictionary from the `morse_code.json` file. The scripts then use this dictionary to perform the requested operation (encryption or decryption).

## How to Use

### s_morse_generator.py

To encrypt a message, open the `s_morse_generator.py` file and edit the `message` variable to the text you want to convert to morse code. Then, run the script:

```
python "Static Morse Code Kit/s_morse_generator.py"
```

### s_morse_cracker.py

To decrypt a message, open the `s_morse_cracker.py` file and edit the `message` variable to the morse code you want to decrypt. Then, run the script:

```
python "Static Morse Code Kit/s_morse_cracker.py"
```

## File Descriptions

- `morse_code.json`: A JSON file containing the morse code dictionary.
- `s_morse_generator.py`: A Python script to encrypt a message into morse code.
- `s_morse_cracker.py`: A Python script to decrypt a morse code message.

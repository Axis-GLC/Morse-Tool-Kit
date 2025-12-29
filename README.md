# Morse Code Kit
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A collection of Python scripts for encrypting and decrypting morse code. This repository contains two versions of the morse code kit: a "Static" version and a "Dynamic" version.

## Setup and Installation

1.  **Clone the repository:**

    ```
    git clone https://github.com/your-username/morse-code-kit.git
    ```

2.  **Navigate to the project directory:**

    ```
    cd morse-code-kit
    ```

3.  **No external libraries are required.** The scripts use only standard Python libraries.

## How to Use

This repository contains two versions of the morse code kit:

### Static Morse Code Kit

This version requires you to directly edit the Python files to change the message you want to work with.

*   **`s_morse_generator.py`**: To encrypt a message, open this file and edit the `message` variable to the text you want to convert to morse code. Then, run the script:

    ```
    python "Static Morse Code Kit/s_morse_generator.py"
    ```

*   **`s_morse_cracker.py`**: To decrypt a message, open this file and edit the `message` variable to the morse code you want to decrypt. Then, run the script:

    ```
    python "Static Morse Code Kit/s_morse_cracker.py"
    ```

### Dynamic Morse Code Kit

This version will interactively ask you for the message you want to work with.

*   **`d_morse_generator.py`**: To encrypt a message, run the script:

    ```
    python "Dynamic Morse Code Kit/d_morse_generator.py"
    ```

    The script will then prompt you to enter the message you want to encrypt. Type your message and press Enter. To quit the script, type `exit`.

*   **`d_morse_cracker.py`**: To decrypt a message, run the script:

    ```
    python "Dynamic Morse Code Kit/d_morse_cracker.py"
    ```

    The script will then prompt you to enter the morse code you want to decrypt. Type the morse code and press Enter. To quit the script, type `exit`.

## How it Works

Both the generator and cracker scripts read the morse code dictionary from the `morse_code.json` file in their respective directories. The scripts then use this dictionary to perform the requested operation (encryption or decryption).

## File Structure

```
.
├── Dynamic Morse Code Kit
│   ├── d_morse_cracker.py
│   ├── d_morse_generator.py
│   ├── INFO.md
│   └── morse_code.json
├── README.md
└── Static Morse Code Kit
    ├── INFO.md
    ├── morse_code.json
    ├── s_morse_cracker.py
    └── s_morse_generator.py
```

## Contributing

Pull requests and issues are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

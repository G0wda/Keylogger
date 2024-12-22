# Keystroke Logger Tool

## Overview
This Keystroke Logger Tool is a Python-based application that captures keyboard input and logs it into a text file (`log.txt`). It uses the `pynput` library to listen to keyboard events and can log alphanumeric characters, special keys, and actions such as backspace, space, and enter.

**Note:** Use this tool responsibly. Unauthorized use of keylogging software may violate privacy laws and ethical guidelines. Always obtain proper consent before deploying this tool.

## Features
- Captures and logs:
  - Alphanumeric keys (letters, numbers).
  - Special keys (e.g., Enter, Backspace, Space).
  - Other keyboard actions (e.g., Control, Shift).
- Logs are saved in a human-readable format.
- Minimal and efficient implementation.

## Prerequisites
- **Python**: Version 3.6 or later.
- **pynput Library**: Install using pip.

## Installation
1. Clone the repository or copy the code into a local Python file.
   ```bash
   git clone https://github.com/G0wda/Keylogger.git
   cd Keylogger
   ```

2. Install the required library:
   ```bash
   pip install pynput
   ```

3. Verify the installation by running the script:
   ```bash
   python Keylogger.py
   ```

## Usage
1. Run the script:
   ```bash
   python Keylogger.py
   ```

2. While the script is running:
   - Any keystrokes will be logged into a file named `log.txt` in the same directory.
   - You can stop the script by manually terminating it (e.g., using `Ctrl+C` in the terminal).

3. View the logged data by opening `log.txt` in a text editor.


## Example Log Output
When the following keys are pressed:
```
Hello World
[BACKSPACE]!
```
The `log.txt` file will contain:
```
Hello World
[BACKSPACE]!
```

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-new-feature
   ```
5. Open a Pull Request.

## Disclaimer
This tool is intended for educational purposes only. Unauthorized use may violate laws or regulations. Ensure compliance with all applicable laws and obtain proper permissions before use.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
For questions or feedback, please contact santhoshgowda9542@gmail.com or open an issue in the repository.

# GhostType - Keylogger & Server Management Tool

GhostType is a Python-based keylogger and server management tool that facilitates remote keystroke logging and monitoring. It allows you to set up a server to collect keystrokes from a client machine running a custom keylogger script. The tool is designed for ethical purposes, such as penetration testing or monitoring systems with authorized consent.

## Features

- **Remote Keylogger Generation**: Easily generate a Python keylogger script that sends keystrokes to a specified server.
- **Server for Keylog Capture**: Set up a server to listen for incoming keystroke data and save it to a log file.
- **IP and Port Validation**: Ensures correct formatting and valid port ranges for connection setup.
- **Socket-based Communication**: Utilizes Python's socket programming to establish communication between the client and server.
- **Error Handling**: Built-in error handling for socket and connection issues.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Generating the Keylogger](#generating-the-keylogger)
  - [Starting the Server](#starting-the-server)
  - [Stopping the Server](#stopping-the-server)
- [Requirements](#requirements)
- [Security](#security)
- [Disclaimer](#disclaimer)
- [License](#license)

## Installation

1. Clone this repository:
```bash
   git https://github.com/udaypali/PRODIGY_CS_04.git
```

2. Navigate to the project directory:
```bash
cd PRODIGY_CS_04
```

3. Install the required Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

# A. Generating the Keylogger

1. Run the script:
```bash
python keylogger.py
```
2. From the main menu, select option 1 to generate a keylogger.

3. Enter the LHOST (your machine's IP address) and LPORT (the port for the server).

4. The keylogger script (remote_keylogger.py) will be generated in the current directory.

# B. Starting the Server

1. Run the script:
```bash
python keylogger.py
```
2. From the main menu, select option 2 to start the server.

3. Enter the LHOST (your machine's IP address) and LPORT (the port to listen on).

4. The server will start and wait for connections from keylogger clients. Keystrokes will be saved in remote_keylog.txt.

# C. Stopping the Server

- To stop the server, use Ctrl + C or close the terminal window.

## Requirements

- Python 3.1
- Dependencies from requirements.txt:
- pynput==1.7.6
- Install dependencies using:

```bash
pip install -r requirements.txt
```

## Security

- Please note that this tool does not use encrypted communication by default. If you're transmitting sensitive data over the network, it's strongly recommended to secure the connection using SSL/TLS.

- You can enable SSL/TLS by modifying the server and client to use Python's ssl module.

## Disclaimer

GhostType is intended for ethical use only. Ensure you have proper authorization before monitoring any system. Unauthorized use of keyloggers may violate laws and result in criminal or civil penalties. The developer of this tool is not responsible for any misuse.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

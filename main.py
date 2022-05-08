import yaml
import os
from sty import fg
import sys
import pick

try:
    # Change to temp pyinstaller's directory (if it's running through pyinstaller).
    os.chdir(sys._MEIPASS)
except:
    # Else try to change the current working directory to the directory of the script.
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except:
        # Already in the script directory
        pass


# Getting the arguments passed to the script.
args = sys.argv

def clear():
    """
    If the operating system is Windows, clear the screen with the cls command, otherwise clear the
    screen with the clear command
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def start_ssh(name,connection):
    """
    It takes a name and a connection dictionary as arguments, and then uses the connection dictionary to
    connect to the server via SSH
    
    :param name: The name of the connection
    :param connection: This is the connection dictionary that contains the connection information
    """
    clear()
    user = connection['user']
    domain = connection['domain']
    port = connection['port']
    print(f"Connecting {fg.green}{name}{fg.rs} at {fg.green}{domain}{fg.rs}:\n")
    os.system(f"ssh {user}@{domain} -p {port}")

# Checking if the file data.yaml exists, and if it does, it loads the data from the file into the sshs variable.
# Otherwise, it prints an error message and exits the script.
if os.path.isfile('data.yaml'):
    with open('data.yaml') as f:
        sshs = yaml.load(f, Loader=yaml.FullLoader)
else:
    print(f"{fg.red}No data.yaml file detected\nPlease make sure that both the script and the data.yaml are in the same directory{fg.rs}")
    input("Press enter to exit...")
    sys.exit()


# Checking if the script was called with an argument, and if it was, then it checks if the argument is
# in the sshs dictionary, and if it is, then it sets the option variable to the value of the argument
# in the sshs dictionary. Otherwise, it creates a menu with the keys of the sshs dictionary as items,
# and then it sets the option variable to the selected item.
if len(args) > 1:
    # Creating a dictionary with the keys of the sshs dictionary as lowercase.
    sshs_lower = {k.casefold(): v for k, v in sshs.items()}
    if args[1].lower() in sshs_lower:
        option = sshs[sshs_lower[args[1].lower()]]
else:
    option, index = pick.pick(list(sshs.keys()),"Connections",indicator=">")


# Calling the start_ssh function with the option and the connection dictionary as arguments.
start_ssh(option, sshs[option])
import yaml
import os
from sty import fg
import sys
import keyboard

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

# It creates a menu with the given title and items, and returns the selected item and its index
class select_menu:
    def __init__(self,title, items, with_exit=False):
        self.with_exit = with_exit
        self.title = title
        self.items = items
        if self.with_exit:
            self.items.append("exit")
        self.selected = 0
        self.start()

    @property
    def result(self):
        #It returns a list of the selected item and the index of the selected item
        return [self.items[self.selected],self.selected]

    def start(self):
        self.show_menu()
        # Bind keys to make the menu interactive.
        keyboard.add_hotkey('up', self.up)
        keyboard.add_hotkey('down', self.down)
        keyboard.wait('enter')
        keyboard.unhook_all_hotkeys()
        clear()
        if self.with_exit:
            self.items.pop(-1)
            if self.selected == len(self.items):
                print("Exiting...")
                sys.exit()

    def show_menu(self):
        clear()
        # Getting the maximum length of the items in the menu.
        for i in range(0, len(self.items)):
            self.items[i] = str(self.items[i])
        max_size = 0
        for item in self.items:
            if max_size<len(item):
                max_size = len(item) + 1
        max_size += 1
        # Printing the title of the menu in green.
        print(f"{fg.green}{self.title}")
        for i in range(0, len(self.items)):
            # Adding spaces to the end of the item to make it the same length as the longest item.
            _item_with_spaces = self.items[i] + (" " * (max_size - len(self.items[i])))
             
            # Printing a new line when the user is on the exit option in order to seperate them.
            if self.with_exit and i == len(self.items)-1:
                print("")
            # Printing a > if the selected item is the current item, otherwise it prints a space.
            print(f"{fg.yellow}>" if self.selected == i else " ",end=" ")
            print(f"{fg.rs}{_item_with_spaces}",end="")
            # Printing a < if the selected item is the current item, otherwise it prints a space.
            print(f"{fg.yellow}<" if self.selected == i else " ") 
            # It resets the color of the text to the default color.
            print(fg.rs,end="")

    def up(self):
        """
        If the selected item is not the first item, then the selected item is decremented by one and the
        menu is shown
        """
        if self.selected == 0:
            return
        self.selected -= 1
        self.show_menu()

    def down(self):
        """
        If the selected item is not the last item in the list, then the selected item is increased by
        one and the menu is shown
        """
        if self.selected == len(self.items)-1:
            return
        self.selected += 1
        self.show_menu()

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

with open('data.yaml') as f:
    sshs = yaml.load(f, Loader=yaml.FullLoader)


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
    option, index = select_menu("Connections",list(sshs.keys()),with_exit=True).result

# Calling the start_ssh function with the option and the connection dictionary as arguments.
start_ssh(option, sshs[option])
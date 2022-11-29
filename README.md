# SSH Manager
A beautiful manager to have all your ssh connections in the same place.

## Install required python packages
```
pip install -r requirments.txt
```
## How to use
You will need to save your ssh connection details in the data.yaml file.
The structure is like this:

```
Server1:                        # Server name (Identifier)
  user: user1                   # User you want to connect with
  domain: example1.com          # Domain name or ip of the server
  port: 22                      # Port of the server
Server2:
  user: root
  domain: 123.123.123.123
  port: 2222

# You can type as many servers as you want
```
## Build Windows
You can also build the code as an executable to run it on PCs without python installed

You can either include the yaml file with the executable, as a result you only need the executable to run the program but you wont be able to add or remove connections and you'll need to rebuild the executable to change them, or you can select not to include the data.yaml so, as a result you'll need to have the data.yaml file in the same directory as the executable whenever you want to run it
To build it for windows, double click on the `build.cmd` in the windows directory. The output will be in the windows directory as `main.exe` 

### Install Linux
Install is implemented only in linux yet
The default install path is ```/opt/ssh-manager```
and the default config path is on user's home_directory/.config/ssh-manager/ (Cant be changed yet)
To install it run:
```
sudo ./linux/install.sh
```
#### Uninstall
```
sudo /opt/ssh-manager/uninstall.sh
```

# SSH Manager
A beautiful manager to have all your ssh connections in the same place.

## How to use
First, you have to download the required packages. You can do it by running the following command:

`pip3 install PyYAML sty pick`

Then, you will need to save your ssh connection details in the data.yaml file.
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
## Build
You can also build the code as an executable to run it on PCs without python installed

You can either include the yaml file the executable as a result you wont be able to add or remove connections and you'll need to rebuild the executable to change them, ot you can select not to include the data.yaml so, as a result you'll need to have the data.yaml file in the same directory as the executable whenever you want to run it

### Windows
To build it for windows, double click on the `build_windows.cmd` in the build directory. The output will be in the build directory as `main.exe` 
### Linux
Not yet implemented

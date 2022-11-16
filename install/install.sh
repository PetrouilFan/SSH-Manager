#!/bin/bash
export installpath=/opt/ssh-manager                                     # Install location
export configpath=$(eval echo ~$SUDO_USER )/.config/ssh-manager         # Configuration location  

if [ "$EUID" -ne 0 ]
  then echo "Please run with sudo"
  exit
fi

cd "${0%/*}"
mkdir -p $installpath
mkdir -p $configpath
cp -r ../../main.py $installpath
cp -r ../../data.yaml $configpath/ssh-manager.yaml

# Create Runner
echo '''
#!/usr/bin/python3
python3 /opt/ssh-manager/main.py
''' > $installpath/runner.sh
chmod +x $installpath/runner.sh
ln -s $installpath/runner.sh /bin/ssh-manager

# Create uninstaller
echo '''
#!/bin/bash
rm -rf /opt/ssh-manager
unlink /bin/ssh-manager
''' > $installpath/uninstall.sh
chmod +x $installpath/uninstall.sh

# Fix permissions
chown -R $SUDO_USER:$SUDO_USER $configpath
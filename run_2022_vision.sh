#!bin/bash
# add this shebang to run this shell script by the bash shell

# change directory to where data_sender.py is located
cd ./
# /home/nvidia/FRC2022-Vision

# if the user does not have executable permissions for data_sender.py, give it to them
if [[ ! -x "data_sender.py" ]]
    then
        echo "user does not have permission to execute the file: data_sender.py, adding execute permission"
        chmod +x "data_sender.py"
        echo "execute permission added"
fi

# run the data_sender.py file
python3 data_sender.py

echo "data_sender.py has been started"

# Steeps for Setup

## Requirements
- S.O linux
- Python3 >= 3.9

## Install Transmission
#### See [TransmissionHowTo](https://help.ubuntu.com/community/TransmissionHowTo)
- sudo apt update
- sudo apt install transmission-cli transmission-common transmission-daemon
- sudo service transmission-daemon [status | stop | start]

## Create enviroment
- python3 -m venv venv
- pip install -r requirements.txt

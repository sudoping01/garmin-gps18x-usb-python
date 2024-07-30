- Make sure that  garmin_gps driver is not blacklisted in modprobe. Comment out any line that says `blacklist garmin_gps` in the following file path.
`sudo nano /etc/modprobe.d/blacklist.conf`
- copy the file 51-garmin.rules to the path /etc/udev/rules.d/: 
`cp 51-garmin.rules /etc/udev/rules.d/`

- Restart the computer or reload the udev rules.
- install dependencies : 
`pip install -r requirements.txt`

- run `gpt.py` : `python gpt.py`




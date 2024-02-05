# shortipy
small web clipboard to copy text to another device.
Written in python based on flask

# preview

![shortipy](https://ibb.co/pvwF7N0/sp.jpg)

# features

* enter text to copy to the web clipboard. you will get a 4 digit number
* use link yourdomain.com/1234 or scan the barcode. you will get your text.

# run as docker

## info

* pull from dockerhub knex666/clipy 
* volume mount container path /clipy/data to persist your DB.
* clipy runs on port 4321: map the port 4321 to any port you like
* or use a reverse proxy
* use /start.sh as entrypoint


## run

   docker run -d --name='clipy' -v '/home/user/clipy':'/clipy/data':'rw' 'knex666/clipy' /start.sh

# run on system

* install python >3
* pull from github
* python -m pip install -r requirements.txt
* python clipy.py or run uwsgi app.ini

# donate
Buy me a Pizza -> https://www.buymeacoffee.com/maschhoff

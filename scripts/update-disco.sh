#!/bin/bash

# check sudo privileges
if [ "$(id -u)" != "0" ]; then
	echo "You do not have sudo privileges"
	exit 1
fi

# get the latest changes from the master branch
supervisorctl stop disco
cd /var/www/DiscoBot && git pull origin master
supervisorctl start disco
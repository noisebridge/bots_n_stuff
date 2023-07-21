#!/bin/bash

echo "Please enter the Discord webhook URI"
read URI

python replace_path.py --uri $URI

echo "Did this post to Discord? (y/N)"
read acknowledge

if [[ $acknowledge == "y" ]]; then
    crontab trash_cron
    echo "All set up!"
else 
    echo "Cron job was not created"
    exit 1
fi

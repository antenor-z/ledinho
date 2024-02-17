#!/bin/bash
if ! pgrep -x "pigpiod" > /dev/null
then
    sudo pigpiod
fi
source venv/bin/activate
gunicorn -c gunicorn_config.py server:app -D

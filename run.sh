#!/bin/bash
sudo pigpiod
source venv/bin/activate
gunicorn -c gunicorn_config.py server:app -D >> log.log 2>&1
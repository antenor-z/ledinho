#!/bin/bash
sudo pigpiod
source venv/bin/activate
gunicorn -c gunicorn_config.py server:app -D >/dev/null 2>/dev/null

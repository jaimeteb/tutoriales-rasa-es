#!/bin/bash

python -m rasa_sdk --actions actions & \
rasa x --no-prompt --enable-api --cors "*"
exec $@

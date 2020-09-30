#!/bin/bash

python -m rasa_sdk --actions actions & rasa run --enable-api
exec $@

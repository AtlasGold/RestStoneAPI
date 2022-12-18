#!/bin/bash
while true
do
        cd /home/ubuntu/RestStoneAPI &&
        gunicorn -b localhost:8000 app:server
        sleep 1
done


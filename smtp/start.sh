#!/bin/bash

name="smtp"
docker stop $name
docker rm $name

docker run --restart=always -d \
    -e "RELAY_NETWORKS=:0.0.0.0/0" \
    --name $name \
    -p 10025:25 \
    namshi/smtp

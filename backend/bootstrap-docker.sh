#!/bin/sh
docker build . -t roubofurto
#docker build . -t roubofurto --platform linux/amd64
docker run -it -p 5002:8080 -d roubofurto
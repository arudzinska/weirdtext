#/bin/bash

docker build -t weirdtext .
docker run -d -p 8000:8000 weirdtext

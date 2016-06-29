#!/bin/bash
# start production server

DOCKER_CONFIG=${DOCKER_CONFIG:-docker-compose-prod.yml}
docker-compose -f $DOCKER_CONFIG up -d
docker-compose -f $DOCKER_CONFIG run --rm -d djangoprod python manage.py twitter_stream_collector --noinput
echo "started"
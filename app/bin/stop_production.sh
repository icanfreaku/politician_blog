#!/bin/bash
# stop production server

DOCKER_CONFIG=${DOCKER_CONFIG:-docker-compose-prod.yml}
docker-compose -f $DOCKER_CONFIG stop
echo "stopped"
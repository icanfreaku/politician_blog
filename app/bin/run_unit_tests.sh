#!/bin/bash
# runs dango unit tests

DOCKER_CONFIG=${DOCKER_CONFIG:-docker-compose.yml}
docker-compose -f $DOCKER_CONFIG run --rm django test